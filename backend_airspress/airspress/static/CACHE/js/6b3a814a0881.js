function ajaxSend(form){$.ajax({type:$(form).attr('method'),url:form.action,data:$(form).serialize(),context:form,success:function(data,status,xhr){if(xhr.status==278){window.location.replace(xhr.getResponseHeader("Location"));}else{$('#signupModal').html(data);}}});}
$(document).on('submit','.signup-form',function(){$.ajax({type:$(this).attr('method'),url:this.action,data:$(this).serialize(),context:this,success:function(data,status,xhr){if(xhr.status==278){window.location.replace(xhr.getResponseHeader("Location"));}else{$('#signupModal').html(data);}}});event.preventDefault();});$(document).on('submit','.login-form',function(){$.ajax({type:$(this).attr('method'),url:this.action,data:$(this).serialize(),context:this,success:function(data,status,xhr){if(xhr.status==278){window.location.replace(xhr.getResponseHeader("Location"));}else{$('#loginModal').html(data);}}});return false;});;(function($){$.pwstrength=function(password){var score=0,length=password.length,upperCase,lowerCase,digits,nonAlpha;if(length<5)score+=0;else if(length<8)score+=5;else if(length<16)score+=10;else score+=15;lowerCase=password.match(/[a-z]/g);if(lowerCase)score+=1;upperCase=password.match(/[A-Z]/g);if(upperCase)score+=5;if(upperCase&&lowerCase)score+=2;digits=password.match(/\d/g);if(digits&&digits.length>1)score+=5;nonAlpha=password.match(/\W/g)
if(nonAlpha)score+=(nonAlpha.length>1)?15:10;if(upperCase&&lowerCase&&digits&&nonAlpha)score+=15;if(password.match(/\s/))score+=10;if(score<15)return 0;if(score<20)return 1;if(score<35)return 2;if(score<50)return 3;return 4;};function updateIndicator(event){var strength=$.pwstrength($(this).val()),options=event.data,klass;klass=options.classes[strength];options.indicator.removeClass(options.indicator.data('pwclass'));options.indicator.data('pwclass',klass);options.indicator.addClass(klass);options.indicator.find(options.label).html(options.texts[strength]);}
$.fn.pwstrength=function(options){var options=$.extend({label:'.label',classes:['pw-very-weak','pw-weak','pw-mediocre','pw-strong','pw-very-strong'],texts:['very weak','weak','mediocre','strong','very strong']},options||{});options.indicator=$('#'+this.data('indicator'));return this.keyup(options,updateIndicator);};})(jQuery);function checkForm(){event.preventDefault();event.stopImmediatePropagation();var box=document.getElementById("checkbox1");if(box.checked){var state=true;document.getElementById("checkbox1").value=state;var form=document.getElementById("signupForm");ajaxSend(form);}else{alert('You must accept the Terms and Conditions.');};calForce();}
document.getElementById("signupForm").onsubmit=checkForm;function calForce(){$('#InputPassword1').pwstrength({label:'.pwdstrength-label'});}
$('document').ready(function(){calForce();});