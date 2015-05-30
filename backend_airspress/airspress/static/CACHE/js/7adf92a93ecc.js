(function(factory){if(typeof define==='function'&&define.amd){define(['jquery'],factory);}else if(typeof exports==='object'){factory(require('jquery'));}else{factory(jQuery);}}(function($){var pluses=/\+/g;function encode(s){return config.raw?s:encodeURIComponent(s);}
function decode(s){return config.raw?s:decodeURIComponent(s);}
function stringifyCookieValue(value){return encode(config.json?JSON.stringify(value):String(value));}
function parseCookieValue(s){if(s.indexOf('"')===0){s=s.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,'\\');}
try{s=decodeURIComponent(s.replace(pluses,' '));return config.json?JSON.parse(s):s;}catch(e){}}
function read(s,converter){var value=config.raw?s:parseCookieValue(s);return $.isFunction(converter)?converter(value):value;}
var config=$.cookie=function(key,value,options){if(value!==undefined&&!$.isFunction(value)){options=$.extend({},config.defaults,options);if(typeof options.expires==='number'){var days=options.expires,t=options.expires=new Date();t.setTime(+t+days*864e+5);}
return(document.cookie=[encode(key),'=',stringifyCookieValue(value),options.expires?'; expires='+options.expires.toUTCString():'',options.path?'; path='+options.path:'',options.domain?'; domain='+options.domain:'',options.secure?'; secure':''].join(''));}
var result=key?undefined:{};var cookies=document.cookie?document.cookie.split('; '):[];for(var i=0,l=cookies.length;i<l;i++){var parts=cookies[i].split('=');var name=decode(parts.shift());var cookie=parts.join('=');if(key&&key===name){result=read(cookie,value);break;}
if(!key&&(cookie=read(cookie))!==undefined){result[name]=cookie;}}
return result;};config.defaults={};$.removeCookie=function(key,options){if($.cookie(key)===undefined){return false;}
$.cookie(key,'',$.extend({},options,{expires:-1}));return!$.cookie(key);};}));var csrftoken=$.cookie('csrftoken');function csrfSafeMethod(method){return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));}
$.ajaxSetup({beforeSend:function(xhr,settings){if(!csrfSafeMethod(settings.type)&&!this.crossDomain){xhr.setRequestHeader("X-CSRFToken",csrftoken);}}});function notify(messageText){var sender="mohamed.coulibali.1@ulaval.ca";var receiver="mohamed.coulibali.1@ulaval.ca"
var urlAction="/account/955CXmoq3f/deals/"
var dealCheck=true;var payload={text:messageText,origin:sender,target:receiver,action:urlAction,isdeal:dealCheck,activityId:"955CXmoq3f"};$.ajax({type:'POST',url:"/account/talk/anyone/",data:payload,success:function(data,status,xhr){console.log('Notification sent !');}});}
function getDateTime(){var now=new Date();var year=now.getFullYear();var month=now.getMonth()+1;var day=now.getDate();var hour=now.getHours();var minute=now.getMinutes();var second=now.getSeconds();if(month.toString().length==1){var month='0'+month;}
if(day.toString().length==1){var day='0'+day;}
if(hour.toString().length==1){var hour='0'+hour;}
if(minute.toString().length==1){var minute='0'+minute;}
if(second.toString().length==1){var second='0'+second;}
var dateTime=day+'/'+month+'/'+year+' '+hour+':'+minute+':'+second;return dateTime;};window.onload=function(){var ref=new Firebase("https://radiant-torch-2520.firebaseio.com/data/airdeals/messages/955CXmoq3f");var ref2=new Firebase("https://radiant-torch-2520.firebaseio.com/data/directMessaging/conversations/");var AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0MzI5NDU0MjksImQiOnsic291cmNlX2lkIjoiOTU1Q1htb3EzZiIsInNvdXJjZSI6ImRlYWxzIiwidXNlcl9pZCI6IkptenFmdExDTDciLCJ1aWQiOiJjdXN0b206Sm16cWZ0TENMNyJ9LCJ2IjowfQ.86fgNcJdBu-7iQ4gLH31Vtpj8I8iVSuuGKRuYnD6NRo";ref.unauth();ref.authWithCustomToken(AUTH_TOKEN,function(error,authData){if(error){console.log("Login Failed!",error);}else{console.log("Login Succeeded!",authData);}});ref2.authWithCustomToken(AUTH_TOKEN,function(error,authData){if(error){console.log("Inbox Failed!",error);}else{console.log("Inbox Succeeded!",authData);}});document.getElementById('SendMessage1').onclick=function(e){e.preventDefault();var newMessageText=document.getElementById('NewMessage1').value;if(newMessageText!==""){ref.push({"sender":"JmzqftLCL7","text":newMessageText,"pub_date":getDateTime()});ref2.update({"inbox":{"senderId":"JmzqftLCL7","senderName":"mohamed.coulibali.1@ulaval.ca","text":newMessageText,"pub_date":Firebase.ServerValue.TIMESTAMP}});document.getElementById('WrapperConversation1').scrollIntoView(false);document.getElementById('NewMessage1').value='';notify(newMessageText);}};document.getElementById('NewMessage1').onkeydown=function Shidori(e){if(e.keyCode==13||e.which==13){e.preventDefault();var newMessageText=document.getElementById('NewMessage1').value;if(newMessageText!==""){ref.push({"sender":"JmzqftLCL7","text":newMessageText,"pub_date":getDateTime()});ref2.update({"inbox":{"senderId":"JmzqftLCL7","senderName":"mohamed.coulibali.1@ulaval.ca","text":newMessageText,"pub_date":Firebase.ServerValue.TIMESTAMP}});document.getElementById('WrapperConversation1').scrollIntoView(false);document.getElementById('NewMessage1').value='';notify(newMessageText);}}};ref.limitToLast(10).on("child_added",function(snapshot){var newMessage=snapshot.val();var conversation=document.getElementById('Conversation1');var wrapper=document.getElementById('WrapperConversation1');var snippet='';var part1='<div class="conversation-item item-left clearfix">\
						<div class="conversation-user">\
							<img class="hidden-xs" src="  http://files.parsetfss.com/ac36d662-47c9-4a1b-a5da-602509e36f9f/tfss-238c63bc-4ce2-46ae-a2da-a6c621f72245-pic1.jpg  " alt=""/>\
						</div>\
						<div class="conversation-body">\
							<div class="name hidden-xs">  mhkane@mit.edu  </div>\
							<div class="time hidden-xs">';var part11='<div class="conversation-item item-right clearfix">\
						<div class="conversation-user">\
							<img class="hidden-xs" src="  http://files.parsetfss.com/ac36d662-47c9-4a1b-a5da-602509e36f9f/tfss-3dd74684-4a9e-46c6-9070-45dffcfc3be8-pic1.jpg  " alt=""/>\
						</div>\
						<div class="conversation-body">\
							<div class="name hidden-xs">  mohamed.coulibali.1@ulaval.ca  </div>\
							<div class="time hidden-xs">';var part2='</div>\
							<div class="text">';var part3='</div>\
						</div>\
					</div>';if(newMessage.sender=="JmzqftLCL7"){snippet=part11+newMessage.pub_date+part2+newMessage.text+part3;}else{snippet=part1+newMessage.pub_date+part2+newMessage.text+part3;}
conversation.innerHTML+=snippet;conversation.scrollTop=conversation.scrollHeight;wrapper.scrollTop=wrapper.scrollHeight;wrapper.style.maxHeight=window.innerHeight;document.getElementById("WrapperConversation1").scrollIntoView(false);});};