function getDateTime(){var now=new Date();var year=now.getFullYear();var month=now.getMonth()+1;var day=now.getDate();var hour=now.getHours();var minute=now.getMinutes();var second=now.getSeconds();if(month.toString().length==1){var month='0'+month;}
if(day.toString().length==1){var day='0'+day;}
if(hour.toString().length==1){var hour='0'+hour;}
if(minute.toString().length==1){var minute='0'+minute;}
if(second.toString().length==1){var second='0'+second;}
var dateTime=day+'/'+month+'/'+year+' '+hour+':'+minute+':'+second;return dateTime;};window.onload=function(){var ref=new Firebase("https://radiant-torch-2520.firebaseio.com/data/airdeals/messages/X9sGdwklD6");var ref2=new Firebase("https://radiant-torch-2520.firebaseio.com/data/directMessaging/conversations/");var AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0MzI2MTMwNjMsImQiOnsic291cmNlX2lkIjoiWDlzR2R3a2xENiIsInNvdXJjZSI6ImRlYWxzIiwidXNlcl9pZCI6IkptenFmdExDTDciLCJ1aWQiOiJjdXN0b206Sm16cWZ0TENMNyJ9LCJ2IjowfQ.zI6BqPaO2pYNWrKHw4fWrq6OO56dyuiyfFMrQ8NvhOQ";ref.unauth();ref.authWithCustomToken(AUTH_TOKEN,function(error,authData){if(error){console.log("Login Failed!",error);}else{console.log("Login Succeeded!",authData);}});ref2.authWithCustomToken(AUTH_TOKEN,function(error,authData){if(error){console.log("Inbox Failed!",error);}else{console.log("Inbox Succeeded!",authData);}});document.getElementById("WrapperConversation1").style.maxHeight=(this.innerHeight-80)+'px';this.onresize=function(){document.getElementById("WrapperConversation1").style.maxHeight=(this.innerHeight-80)+'px';};document.getElementById('SendMessage1').onclick=function(e){e.preventDefault();var newMessageText=document.getElementById('NewMessage1').value;if(newMessageText!==""){ref.push({"sender":"JmzqftLCL7","text":newMessageText,"pub_date":getDateTime()});ref2.update({"inbox":{"senderId":"JmzqftLCL7","senderName":"mohamed.coulibali.1@ulaval.ca","text":newMessageText,"pub_date":Firebase.ServerValue.TIMESTAMP}});document.getElementById('NewMessage1').value='';}};document.getElementById('NewMessage1').onkeydown=function Shidori(e){if(e.keyCode==13||e.which==13){e.preventDefault();var newMessageText=document.getElementById('NewMessage1').value;if(newMessageText!==""){ref.push({"sender":"JmzqftLCL7","text":newMessageText,"pub_date":getDateTime()});ref2.update({"inbox":{"senderId":"JmzqftLCL7","senderName":"mohamed.coulibali.1@ulaval.ca","text":newMessageText,"pub_date":Firebase.ServerValue.TIMESTAMP}});document.getElementById('NewMessage1').value='';}}};ref.limitToLast(10).on("child_added",function(snapshot){var newMessage=snapshot.val();var conversation=document.getElementById('Conversation1');var wrapper=document.getElementById('WrapperConversation1');var snippet='';var part1='<div class="conversation-item item-left clearfix">\
						<div class="conversation-user">\
							<img class="hidden-xs" src="    " alt=""/>\
						</div>\
						<div class="conversation-body">\
							<div class="name hidden-xs">  aboubacar.karim.1@ulaval.ca  </div>\
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