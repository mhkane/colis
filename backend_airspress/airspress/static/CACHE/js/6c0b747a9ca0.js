function getDateTime(){var now=new Date();var year=now.getFullYear();var month=now.getMonth()+1;var day=now.getDate();var hour=now.getHours();var minute=now.getMinutes();var second=now.getSeconds();if(month.toString().length==1){var month='0'+month;}
if(day.toString().length==1){var day='0'+day;}
if(hour.toString().length==1){var hour='0'+hour;}
if(minute.toString().length==1){var minute='0'+minute;}
if(second.toString().length==1){var second='0'+second;}
var dateTime=day+'/'+month+'/'+year+' '+hour+':'+minute+':'+second;return dateTime;};window.onload=function(){var ref=new Firebase("https://radiant-torch-2520.firebaseio.com/messages/FvnjqsZXmy");var AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0MzE0NDMxOTQsImQiOnsic291cmNlX2lkIjoiRnZuanFzWlhteSIsInNvdXJjZSI6ImRlYWxzIiwidXNlcl9pZCI6IjlsVExmM0dQZzEiLCJ1aWQiOiJjdXN0b206OWxUTGYzR1BnMSJ9LCJ2IjowfQ.bAzRuVzXJ_IbLUfClHMkOSSUGdDgzkbVBTRCCiIn5zw";ref.unauth();ref.authWithCustomToken(AUTH_TOKEN,function(error,authData){if(error){console.log("Login Failed!",error);}else{console.log("Login Succeeded!",authData);}});document.getElementById("WrapperConversation1").style.maxHeight=(this.innerHeight-80)+'px';this.onresize=function(){document.getElementById("WrapperConversation1").style.maxHeight=(this.innerHeight-80)+'px';};document.getElementById('SendMessage1').onclick=function(e){e.preventDefault();var newMessageText=document.getElementById('NewMessage1').value;if(newMessageText!==""){ref.push({"sender":"9lTLf3GPg1","text":newMessageText,"pub_date":getDateTime()});document.getElementById('NewMessage1').value='';}};document.getElementById('NewMessage1').onkeydown=function Shidori(e){if(e.keyCode==13||e.which==13){e.preventDefault();var newMessageText=document.getElementById('NewMessage1').value;if(newMessageText!==""){ref.push({"sender":"9lTLf3GPg1","text":newMessageText,"pub_date":getDateTime()});document.getElementById('NewMessage1').value='';}}};ref.limitToLast(10).on("child_added",function(snapshot){var newMessage=snapshot.val();var conversation=document.getElementById('Conversation1');var wrapper=document.getElementById('WrapperConversation1');var snippet='';var part1='<div class="conversation-item item-left clearfix">\
						<div class="conversation-user">\
							<img src="  http://files.parsetfss.com/ac36d662-47c9-4a1b-a5da-602509e36f9f/tfss-640cd423-99bd-4e49-97bf-41b46eabea2b-pic1.jpg  " alt=""/>\
						</div>\
						<div class="conversation-body">\
							<div class="name">  Mohamed_K.  </div>\
							<div class="time hidden-xs">';var part11='<div class="conversation-item item-right clearfix">\
						<div class="conversation-user">\
							<img src="  http://files.parsetfss.com/ac36d662-47c9-4a1b-a5da-602509e36f9f/tfss-28475a36-db4d-4fad-b89f-193ecd9e51d7-pic1.jpg  " alt=""/>\
						</div>\
						<div class="conversation-body">\
							<div class="name">  mohamed.coulibali.1@ulaval.ca  </div>\
							<div class="time hidden-xs">';var part2='</div>\
							<div class="text">';var part3='</div>\
						</div>\
					</div>';if(newMessage.sender=="9lTLf3GPg1"){snippet=part11+newMessage.pub_date+part2+newMessage.text+part3;}else{snippet=part1+newMessage.pub_date+part2+newMessage.text+part3;}
conversation.innerHTML+=snippet;conversation.scrollTop=conversation.scrollHeight;wrapper.scrollTop=wrapper.scrollHeight;wrapper.style.maxHeight=window.innerHeight;});};