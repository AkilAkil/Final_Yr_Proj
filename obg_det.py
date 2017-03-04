import cv2
import numpy as np
#import time
detector=cv2.SIFT()
FLANN_INDEX_KDTREE=0
flannParam=dict(algorithm=FLANN_INDEX_KDTREE,tree=5)
flann=cv2.FlannBasedMatcher(flannParam,{})
trainImg=cv2.imread('/home/akil/Downloads/crazy1.png8')
trainKP,trainDecs=detector.detectAndCompute(trainImg,None)
cam=cv2.VideoCapture('/home/akil/Downloads/trainvid.mp4')
#time.sleep(2)
while True:
    ret,QueryImgBGR=cam.read()
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.knnMatch(queryDesc,trainDecs,k=2)

    goodMatch=[]
    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)
    if(len(goodMatch)>12):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        nslice, h,w=trainImg.shape
        trainingBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainingBorder,H)
        cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(0,255,0),5)
    else:
        print "Not enough matches-%d/%d"%(len(goodMatch),30)
    cv2.imshow('result',QueryImgBGR)
    cv2.waitKey(10)
