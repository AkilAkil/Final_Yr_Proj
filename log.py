'''import xlsxwriter
from datetime import datetime

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
i = 1

# Iterate over the data and write it out row by row.
#for item, cost in (expenses):
#def store(i)
for i in range(10):
    worksheet.write(row, col,i)
    worksheet.write(row, col + 1,str(datetime.now()))
    row += 1
    i +=1

workbook.close()'''
from datetime import datetime
import csv
writer = open('test.csv', 'r')

def store(i,k):
#for i in range(10):
        #print "Hii %s" % str(datetime.now())
        for row in writer:
            ar = csv.writer(writer, delimiter=',')
            data = [i,str(datetime.now())]
            row[k] = data
            writer.writerow(data)