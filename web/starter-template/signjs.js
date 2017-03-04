$(function() {
  "use strict"

  var name;
  var loggedin = $(".loggedin").hide();
  var t = 500;

  function store() {
    name = $("input#username").val();
  }

  function init() {
    $("input[type='submit']").on("click", function() {
      store();
      $(".login_inner, .login_inner__avatar").animate({
        'opacity': '0'
      }, t);
      setTimeout(function() {
        $(".login_inner__check").css({
          'opacity': '1',
          'animation': 'spinner 4s 0s linear',
          'transition': 'all ease 3s'
        });
      });
      setTimeout(function() {
        $(".login_inner__check--complete").find('i').animate({
          'opacity': '1'
        }, 500);
      }, 4200);
      setTimeout(function() {
        $(".login").fadeOut(500, function() {
          $(this).remove();
        });
      }, 5000);
      setTimeout(function() {
        loggedin.fadeIn(t, function() {
          $(this).show();
          $(this).find('h2').html("Welcome " + name);
        });
      }, 5500);
      setTimeout(function() {
        $(".loggedin h2").animate({
          'opacity': '1'
        }, t);
      }, 6000);
    });
  };
  init();
});