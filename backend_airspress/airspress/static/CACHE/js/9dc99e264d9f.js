(function(e){function u(s,o){var u,a,f;if((u=e(s))[t]==0)return n;a=u[i]()[r];switch(o.anchor){case"middle":f=a-(e(window).height()-u.outerHeight())/2;break;default:case r:f=Math.max(a,0)}return typeof o[i]=="function"?f-=o[i]():f-=o[i],f}var t="length",n=null,r="top",i="offset",s="click.scrolly",o=e(window);e.fn.scrolly=function(i){var o,a,f,l,c=e(this);if(this[t]==0)return c;if(this[t]>1){for(o=0;o<this[t];o++)e(this[o]).scrolly(i);return c}l=n,f=c.attr("href");if(f.charAt(0)!="#"||f[t]<2)return c;a=jQuery.extend({anchor:r,easing:"swing",offset:0,parent:e("body,html"),pollOnce:!1,speed:1e3},i),a.pollOnce&&(l=u(f,a)),c.off(s).on(s,function(e){var t=l!==n?l:u(f,a);t!==n&&(e.preventDefault(),a.parent.stop().animate({scrollTop:t},a.speed,a.easing))})}})(jQuery);(function(e){var t="openerActiveClass",n="click touchend",r="left",i="doCollapseAll",s="position",o="trigger",u="disableSelection_dropotron",a="addClass",f="doCollapse",l=!1,c="outerWidth",h="removeClass",p="preventDefault",d="length",v="dropotron",m="clearTimeout",g="right",y="parent",b=!0,w="speed",E="none",S="stopPropagation",x="doExpand",T=":visible",N="absolute",C="css",k="center",L="toggle",A="baseZIndex",O="offsetX",M="alignment",_="submenuClassPrefix",D="children",P="hover",H="relative",B="doToggle",j="ul",F="z-index",I="opacity",q="find",R="opener",U="px",z=null,W="hide",X="offset",V="detach",$="fast";e.fn[u]=function(){return e(this)[C]("user-select",E)[C]("-khtml-user-select",E)[C]("-moz-user-select",E)[C]("-o-user-select",E)[C]("-webkit-user-select",E)},e.fn[v]=function(t){var n;if(this[d]==0)return e(this);if(this[d]>1)for(n=0;n<this[d];n++)e(this[n])[v](t);return e[v](e.extend({selectorParent:e(this)},t))},e[v]=function(E){var et=e.extend({selectorParent:z,baseZIndex:1e3,menuClass:v,expandMode:P,hoverDelay:150,hideDelay:250,openerClass:R,openerActiveClass:"active",submenuClassPrefix:"level-",mode:"fade",speed:$,easing:"swing",alignment:r,offsetX:0,offsetY:0,globalOffsetY:0,IEOffsetX:0,IEOffsetY:0,noOpenerFade:b,detach:b,cloneOnDetach:b},E),tt=et.selectorParent,nt=tt[q](j),rt=e("body"),it=e("body,html"),st=e(window),ot=l,ut=z,at=z;tt.on(i,function(){nt[o](f)}),nt.each(function(){var i=e(this),d=i[y]();et.hideDelay>0&&i.add(d).on("mouseleave",function(){window[m](at),at=window.setTimeout(function(){i[o](f)},et.hideDelay)}),i[u]()[W]()[a](et.menuClass)[C](s,N).on("mouseenter",function(){window[m](at)}).on(x,function(){var n,u,p,v,E,S,x,_,D,P,B;if(i.is(T))return l;window[m](at),nt.each(function(){var t=e(this);e.contains(t.get(0),d.get(0))||t[o](f)}),n=d[X](),u=d[s](),p=d[y]()[s](),v=d[c](),E=i[c](),S=i[C](F)==et[A];if(S){et[V]?x=n:x=u,P=x.top+d.outerHeight()+et.globalOffsetY,_=et[M],i[h](r)[h](g)[h](k);switch(et[M]){case g:D=x[r]-E+v,D<0&&(D=x[r],_=r);break;case k:D=x[r]-Math.floor((E-v)/2),D<0?(D=x[r],_=r):D+E>st.width()&&(D=x[r]-E+v,_=g);break;case r:default:D=x[r],D+E>st.width()&&(D=x[r]-E+v,_=g)}i[a](_)}else{d[C](s)==H||d[C](s)==N?(P=et.offsetY,D=-1*u[r]):(P=u.top+et.offsetY,D=0);switch(et[M]){case g:D+=-1*d[y]()[c]()+et[O];break;case k:case r:default:D+=d[y]()[c]()+et[O]}}navigator.userAgent.match(/MSIE ([0-9]+)\./)&&RegExp.$1<8&&(D+=et.IEOffsetX,P+=et.IEOffsetY),i[C](r,D+U)[C]("top",P+U)[C](I,"0.01").show(),B=l,d[C](s)==H||d[C](s)==N?D=-1*u[r]:D=0,i[X]()[r]<0?(D+=d[y]()[c]()-et[O],B=b):i[X]()[r]+E>st.width()&&(D+=-1*d[y]()[c]()-et[O],B=b),B&&i[C](r,D+U),i[W]()[C](I,"1");switch(et.mode){case"zoom":ot=b,d[a](et[t]),i.animate({width:L,height:L},et[w],et.easing,function(){ot=l});break;case"slide":ot=b,d[a](et[t]),i.animate({height:L},et[w],et.easing,function(){ot=l});break;case"fade":ot=b,S&&!et.noOpenerFade?(et[w]=="slow"?B=80:et[w]==$?B=40:B=Math.floor(et[w]/2),d.fadeTo(B,.01,function(){d[a](et[t]),d.fadeTo(et[w],1),i.fadeIn(et[w],function(){ot=l})})):(d[a](et[t]),d.fadeTo(et[w],1),i.fadeIn(et[w],function(){ot=l}));break;case"instant":default:d[a](et[t]),i.show()}return l}).on(f,function(){return i.is(T)?(i[W](),d[h](et[t]),i[q]("."+et[t])[h](et[t]),i[q](j)[W](),l):l}).on(B,function(){return i.is(T)?i[o](f):i[o](x),l}),d[u]()[a](R)[C]("cursor","pointer").on(n,function(e){if(ot)return;e[p](),e[S](),i[o](B)}),et.expandMode==P&&d[P](function(){if(ot)return;ut=window.setTimeout(function(){i[o](x)},et.hoverDelay)},function(){window[m](ut)})}),nt[q]("a")[C]("display","block").on(n,function(t){if(ot)return;e(this).attr("href")[d]<1&&t[p]()}),tt[q]("li")[C]("white-space","nowrap").each(function(){var t=e(this),r=t[D]("a"),s=t[D](j),u=r.attr("href");r.on(n,function(e){u[d]==0||u=="#"?e[p]():e[S]()}),r[d]>0&&s[d]==0&&t.on(n,function(e){if(ot)return;tt[o](i),e[S]()})}),tt[D]("li").each(function(){var t,n,r,i,s=e(this),o=s[D](j);if(o[d]>0){et[V]&&(et.cloneOnDetach&&(t=o.clone(),t.attr("class","")[W]().appendTo(o[y]())),o[V]().appendTo(rt));for(n=et[A],r=1,i=o;i[d]>0;r++)i[C](F,n++),et[_]&&i[a](et[_]+(n-1-et[A])),i=i[q]("> li > ul")}}),st.on("scroll",function(){tt[o](i)}).on("keypress",function(e){!ot&&e.keyCode==27&&(e[p](),tt[o](i))}),it.on(n,function(){ot||tt[o](i)})}})(jQuery);!function(t){function e(t,e,n){return"string"==typeof t&&("%"==t.slice(-1)?t=parseInt(t.substring(0,t.length-1))/100*e:"vh"==t.slice(-2)?t=parseInt(t.substring(0,t.length-2))/100*n:"px"==t.slice(-2)&&(t=parseInt(t.substring(0,t.length-2)))),t}var n=t(window),i=1,o={};n.on("scroll",function(){var e=n.scrollTop();t.map(o,function(t){window.clearTimeout(t.timeoutId),t.timeoutId=window.setTimeout(function(){t.handler(e)},t.options.delay)})}).on("load",function(){n.trigger("scroll")}),jQuery.fn.scrollex=function(l){var s=t(this);if(0==this.length)return s;if(this.length>1){for(var r=0;r<this.length;r++)t(this[r]).scrollex(l);return s}if(s.data("_scrollexId"))return s;var a,u,h,c,p;switch(a=i++,u=jQuery.extend({top:0,bottom:0,delay:0,mode:"default",enter:null,leave:null,initialize:null,terminate:null,scroll:null},l),u.mode){case"top":h=function(t,e,n,i,o){return t>=i&&o>=t};break;case"bottom":h=function(t,e,n,i,o){return n>=i&&o>=n};break;case"middle":h=function(t,e,n,i,o){return e>=i&&o>=e};break;case"top-only":h=function(t,e,n,i,o){return i>=t&&n>=i};break;case"bottom-only":h=function(t,e,n,i,o){return n>=o&&o>=t};break;default:case"default":h=function(t,e,n,i,o){return n>=i&&o>=t}}return c=function(t){var i,o,l,s,r,a,u=this.state,h=!1,c=this.$element.offset();i=n.height(),o=t+i/2,l=t+i,s=this.$element.outerHeight(),r=c.top+e(this.options.top,s,i),a=c.top+s-e(this.options.bottom,s,i),h=this.test(t,o,l,r,a),h!=u&&(this.state=h,h?this.options.enter&&this.options.enter.apply(this.element):this.options.leave&&this.options.leave.apply(this.element)),this.options.scroll&&this.options.scroll.apply(this.element,[(o-r)/(a-r)])},p={id:a,options:u,test:h,handler:c,state:null,element:this,$element:s,timeoutId:null},o[a]=p,s.data("_scrollexId",p.id),p.options.initialize&&p.options.initialize.apply(this),s},jQuery.fn.unscrollex=function(){var e=t(this);if(0==this.length)return e;if(this.length>1){for(var n=0;n<this.length;n++)t(this[n]).unscrollex();return e}var i,l;return(i=e.data("_scrollexId"))?(l=o[i],window.clearTimeout(l.timeoutId),delete o[i],e.removeData("_scrollexId"),l.options.terminate&&l.options.terminate.apply(this),e):e}}(jQuery);var skel=function(){"use strict";var t={breakpointIds:null,events:{},isInit:!1,obj:{attachments:{},breakpoints:{},head:null,states:{}},sd:"/",state:null,stateHandlers:{},stateId:"",vars:{},DOMReady:null,indexOf:null,isArray:null,iterate:null,matchesMedia:null,extend:function(e,n){t.iterate(n,function(i){t.isArray(n[i])?(t.isArray(e[i])||(e[i]=[]),t.extend(e[i],n[i])):"object"==typeof n[i]?("object"!=typeof e[i]&&(e[i]={}),t.extend(e[i],n[i])):e[i]=n[i]})},newStyle:function(t){var e=document.createElement("style");return e.type="text/css",e.innerHTML=t,e},_canUse:null,canUse:function(e){t._canUse||(t._canUse=document.createElement("div"));var n=t._canUse.style,i=e.charAt(0).toUpperCase()+e.slice(1);return e in n||"Moz"+i in n||"Webkit"+i in n||"O"+i in n||"ms"+i in n},on:function(e,n){var i=e.split(/[\s]+/);return t.iterate(i,function(e){var r=i[e];if(t.isInit){if("init"==r)return void n();if("change"==r)n();else if("+"==r.charAt(0)&&t.obj.breakpoints[r.substring(1)].active)n();else if("!"==r.charAt(0)&&!t.obj.breakpoints[r.substring(1)].active)return void n()}t.events[r]||(t.events[r]=[]),t.events[r].push(n)}),t},trigger:function(e){return t.events[e]&&0!=t.events[e].length?(t.iterate(t.events[e],function(n){t.events[e][n]()}),t):void 0},breakpoint:function(e){return t.obj.breakpoints[e]},breakpoints:function(e){function n(t,e){this.name=this.id=t,this.media=e,this.active=!1,this.wasActive=!1}return n.prototype.sync=function(){if(t.matchesMedia(this.media)){if(this.active)return;this.wasActive=!1,this.active=!0}else{if(!this.active)return;this.wasActive=!0,this.active=!1}},t.iterate(e,function(i){t.obj.breakpoints[i]=new n(i,e[i])}),window.setTimeout(function(){t.poll()},0),t},addStateHandler:function(e,n){t.stateHandlers[e]=n},callStateHandler:function(e){var n=t.stateHandlers[e]();t.iterate(n,function(e){t.state.attachments.push(n[e])})},changeState:function(e){t.vars.lastStateId=t.stateId,t.stateId=e,t.breakpointIds=t.stateId===t.sd?[]:t.stateId.substring(1).split(t.sd),t.obj.states[t.stateId]?t.state=t.obj.states[t.stateId]:(t.obj.states[t.stateId]={attachments:[]},t.state=t.obj.states[t.stateId],t.iterate(t.stateHandlers,t.callStateHandler)),t.detachAll(t.state.attachments),t.attachAll(t.state.attachments),t.vars.stateId=t.stateId,t.vars.state=t.state,t.trigger("change"),t.iterate(t.obj.breakpoints,function(e){t.obj.breakpoints[e].active?t.obj.breakpoints[e].wasActive||t.trigger("+"+e):t.obj.breakpoints[e].wasActive&&t.trigger("-"+e)})},generateStateConfig:function(e,n){var i={};return t.extend(i,e),t.iterate(t.breakpointIds,function(e){t.extend(i,n[t.breakpointIds[e]])}),i},getStateId:function(){var e="";return t.iterate(t.obj.breakpoints,function(n){var i=t.obj.breakpoints[n];i.sync(),i.active&&(e+=t.sd+i.id)}),e},poll:function(){var e="";e=t.getStateId(),""===e&&(e=t.sd),e!==t.stateId&&t.changeState(e)},_attach:null,attach:function(e){var n=t.obj.head,i=e.element;return i.parentNode&&i.parentNode.tagName?!1:(t._attach||(t._attach=n.firstChild),n.insertBefore(i,t._attach.nextSibling),e.permanent&&(t._attach=i),!0)},attachAll:function(e){var n=[];t.iterate(e,function(t){n[e[t].priority]||(n[e[t].priority]=[]),n[e[t].priority].push(e[t])}),n.reverse(),t.iterate(n,function(e){t.iterate(n[e],function(i){t.attach(n[e][i])})})},detach:function(t){var e=t.element;return t.permanent||!e.parentNode||e.parentNode&&!e.parentNode.tagName?!1:(e.parentNode.removeChild(e),!0)},detachAll:function(e){var n={};t.iterate(e,function(t){n[e[t].id]=!0}),t.iterate(t.obj.attachments,function(e){e in n||t.detach(t.obj.attachments[e])})},attachment:function(e){return e in t.obj.attachments?t.obj.attachments[e]:null},newAttachment:function(e,n,i,r){return t.obj.attachments[e]={id:e,element:n,priority:i,permanent:r}},init:function(){t.initMethods(),t.initVars(),t.initEvents(),t.obj.head=document.getElementsByTagName("head")[0],t.isInit=!0,t.trigger("init")},initEvents:function(){t.on("resize",function(){t.poll()}),t.on("orientationChange",function(){t.poll()}),t.DOMReady(function(){t.trigger("ready")}),window.onload&&t.on("load",window.onload),window.onload=function(){t.trigger("load")},window.onresize&&t.on("resize",window.onresize),window.onresize=function(){t.trigger("resize")},window.onorientationchange&&t.on("orientationChange",window.onorientationchange),window.onorientationchange=function(){t.trigger("orientationChange")}},initMethods:function(){document.addEventListener?!function(e,n){t.DOMReady=n()}("domready",function(){function t(t){for(a=1;t=n.shift();)t()}var e,n=[],i=document,r="DOMContentLoaded",a=/^loaded|^c/.test(i.readyState);return i.addEventListener(r,e=function(){i.removeEventListener(r,e),t()}),function(t){a?t():n.push(t)}}):!function(e,n){t.DOMReady=n()}("domready",function(t){function e(t){for(h=1;t=i.shift();)t()}var n,i=[],r=!1,a=document,o=a.documentElement,s=o.doScroll,c="DOMContentLoaded",d="addEventListener",u="onreadystatechange",l="readyState",f=s?/^loaded|^c/:/^loaded|c/,h=f.test(a[l]);return a[d]&&a[d](c,n=function(){a.removeEventListener(c,n,r),e()},r),s&&a.attachEvent(u,n=function(){/^c/.test(a[l])&&(a.detachEvent(u,n),e())}),t=s?function(e){self!=top?h?e():i.push(e):function(){try{o.doScroll("left")}catch(n){return setTimeout(function(){t(e)},50)}e()}()}:function(t){h?t():i.push(t)}}),t.indexOf=Array.prototype.indexOf?function(t,e){return t.indexOf(e)}:function(t,e){if("string"==typeof t)return t.indexOf(e);var n,i,r=e?e:0;if(!this)throw new TypeError;if(i=this.length,0===i||r>=i)return-1;for(0>r&&(r=i-Math.abs(r)),n=r;i>n;n++)if(this[n]===t)return n;return-1},t.isArray=Array.isArray?function(t){return Array.isArray(t)}:function(t){return"[object Array]"===Object.prototype.toString.call(t)},t.iterate=Object.keys?function(t,e){if(!t)return[];var n,i=Object.keys(t);for(n=0;i[n]&&e(i[n],t[i[n]])!==!1;n++);}:function(t,e){if(!t)return[];var n;for(n in t)if(Object.prototype.hasOwnProperty.call(t,n)&&e(n,t[n])===!1)break},t.matchesMedia=window.matchMedia?function(t){return""==t?!0:window.matchMedia(t).matches}:window.styleMedia||window.media?function(t){if(""==t)return!0;var e=window.styleMedia||window.media;return e.matchMedium(t||"all")}:window.getComputedStyle?function(t){if(""==t)return!0;var e=document.createElement("style"),n=document.getElementsByTagName("script")[0],i=null;e.type="text/css",e.id="matchmediajs-test",n.parentNode.insertBefore(e,n),i="getComputedStyle"in window&&window.getComputedStyle(e,null)||e.currentStyle;var r="@media "+t+"{ #matchmediajs-test { width: 1px; } }";return e.styleSheet?e.styleSheet.cssText=r:e.textContent=r,"1px"===i.width}:function(t){if(""==t)return!0;var e,n,i,r,a={"min-width":null,"max-width":null},o=!1;n=t.split(/\s+and\s+/);for(r in n)e=n[r],"("==e.charAt(0)&&(e=e.substring(1,e.length-1),i=e.split(/:\s+/),2==i.length&&(a[i[0].replace(/^\s+|\s+$/g,"")]=parseInt(i[1]),o=!0));if(!o)return!1;var s=document.documentElement.clientWidth,c=document.documentElement.clientHeight;return null!==a["min-width"]&&s<a["min-width"]||null!==a["max-width"]&&s>a["max-width"]||null!==a["min-height"]&&c<a["min-height"]||null!==a["max-height"]&&c>a["max-height"]?!1:!0},navigator.userAgent.match(/MSIE ([0-9]+)/)&&RegExp.$1<9&&(t.newStyle=function(t){var e=document.createElement("span");return e.innerHTML='&nbsp;<style type="text/css">'+t+"</style>",e})},initVars:function(){var e,n,i,r=navigator.userAgent;e="other",n=0,i=[["firefox",/Firefox\/([0-9\.]+)/],["bb",/BlackBerry.+Version\/([0-9\.]+)/],["bb",/BB[0-9]+.+Version\/([0-9\.]+)/],["opera",/OPR\/([0-9\.]+)/],["opera",/Opera\/([0-9\.]+)/],["edge",/Edge\/([0-9\.]+)/],["safari",/Version\/([0-9\.]+).+Safari/],["chrome",/Chrome\/([0-9\.]+)/],["ie",/MSIE ([0-9]+)/],["ie",/Trident\/.+rv:([0-9]+)/]],t.iterate(i,function(t,i){return r.match(i[1])?(e=i[0],n=parseFloat(RegExp.$1),!1):void 0}),t.vars.browser=e,t.vars.browserVersion=n,e="other",n=0,i=[["ios",/([0-9_]+) like Mac OS X/,function(t){return t.replace("_",".").replace("_","")}],["ios",/CPU like Mac OS X/,function(t){return 0}],["android",/Android ([0-9\.]+)/,null],["mac",/Macintosh.+Mac OS X ([0-9_]+)/,function(t){return t.replace("_",".").replace("_","")}],["wp",/Windows Phone ([0-9\.]+)/,null],["windows",/Windows NT ([0-9\.]+)/,null],["bb",/BlackBerry.+Version\/([0-9\.]+)/,null],["bb",/BB[0-9]+.+Version\/([0-9\.]+)/,null]],t.iterate(i,function(t,i){return r.match(i[1])?(e=i[0],n=parseFloat(i[2]?i[2](RegExp.$1):RegExp.$1),!1):void 0}),t.vars.os=e,t.vars.osVersion=n,t.vars.IEVersion="ie"==t.vars.browser?t.vars.browserVersion:99,t.vars.touch="wp"==t.vars.os?navigator.msMaxTouchPoints>0:!!("ontouchstart"in window),t.vars.mobile="wp"==t.vars.os||"android"==t.vars.os||"ios"==t.vars.os||"bb"==t.vars.os}};return t.init(),t}();!function(t,e){"function"==typeof define&&define.amd?define([],e):"object"==typeof exports?module.exports=e():t.skel=e()}(this,function(){return skel});(function($){$.fn.navList=function(){var $this=$(this);$a=$this.find('a'),b=[];$a.each(function(){var $this=$(this),indent=Math.max(0,$this.parents('li').length-1),href=$this.attr('href'),target=$this.attr('target');b.push('<a '+'class="link depth-'+indent+'"'+
((typeof target!=='undefined'&&target!='')?' target="'+target+'"':'')+
((typeof href!=='undefined'&&href!='')?' href="'+href+'"':'')+'>'+'<span class="indent-'+indent+'"></span>'+
$this.text()+'</a>');});return b.join('');};$.fn.panel=function(userConfig){if(this.length==0)
return $this;if(this.length>1){for(var i=0;i<this.length;i++)
$(this[i]).panel(userConfig);return $this;}
var $this=$(this),$body=$('body'),$window=$(window),id=$this.attr('id'),config;config=$.extend({delay:0,hideOnClick:false,hideOnEscape:false,hideOnSwipe:false,resetScroll:false,resetForms:false,side:null,target:$this,visibleClass:'visible'},userConfig);if(typeof config.target!='jQuery')
config.target=$(config.target);$this._hide=function(event){if(!config.target.hasClass(config.visibleClass))
return;if(event){event.preventDefault();event.stopPropagation();}
config.target.removeClass(config.visibleClass);window.setTimeout(function(){if(config.resetScroll)
$this.scrollTop(0);if(config.resetForms)
$this.find('form').each(function(){this.reset();});},config.delay);};$this.css('-ms-overflow-style','-ms-autohiding-scrollbar').css('-webkit-overflow-scrolling','touch');if(config.hideOnClick)
$this.find('a').css('-webkit-tap-highlight-color','rgba(0,0,0,0)').on('click',function(event){var $a=$(this),href=$a.attr('href'),target=$a.attr('target');if(!href||href=='#'||href==''||href=='#'+id)
return;event.preventDefault();event.stopPropagation();$this._hide();window.setTimeout(function(){if(target=='_blank')
window.open(href);else
window.location.href=href;},config.delay+10);});$this.on('touchstart',function(event){$this.touchPosX=event.originalEvent.touches[0].pageX;$this.touchPosY=event.originalEvent.touches[0].pageY;})
$this.on('touchmove',function(event){if($this.touchPosX===null||$this.touchPosY===null)
return;var diffX=$this.touchPosX-event.originalEvent.touches[0].pageX,diffY=$this.touchPosY-event.originalEvent.touches[0].pageY,th=$this.outerHeight(),ts=($this.get(0).scrollHeight-$this.scrollTop());if(config.hideOnSwipe){var result=false,boundary=20,delta=50;switch(config.side){case'left':result=(diffY<boundary&&diffY>(-1*boundary))&&(diffX>delta);break;case'right':result=(diffY<boundary&&diffY>(-1*boundary))&&(diffX<(-1*delta));break;case'top':result=(diffX<boundary&&diffX>(-1*boundary))&&(diffY>delta);break;case'bottom':result=(diffX<boundary&&diffX>(-1*boundary))&&(diffY<(-1*delta));break;default:break;}
if(result){$this.touchPosX=null;$this.touchPosY=null;$this._hide();return false;}}
if(($this.scrollTop()<0&&diffY<0)||(ts>(th-2)&&ts<(th+2)&&diffY>0)){event.preventDefault();event.stopPropagation();}});$this.on('click touchend touchstart touchmove',function(event){event.stopPropagation();});$this.on('click','a[href="#'+id+'"]',function(event){event.preventDefault();event.stopPropagation();config.target.removeClass(config.visibleClass);});$body.on('click touchend',function(event){$this._hide(event);});$body.on('click','a[href="#'+id+'"]',function(event){event.preventDefault();event.stopPropagation();config.target.toggleClass(config.visibleClass);});if(config.hideOnEscape)
$window.on('keydown',function(event){if(event.keyCode==27)
$this._hide(event);});return $this;};$.fn.placeholder=function(){if(typeof(document.createElement('input')).placeholder!='undefined')
return $(this);if(this.length==0)
return $this;if(this.length>1){for(var i=0;i<this.length;i++)
$(this[i]).placeholder();return $this;}
var $this=$(this);$this.find('input[type=text],textarea').each(function(){var i=$(this);if(i.val()==''||i.val()==i.attr('placeholder'))
i.addClass('polyfill-placeholder').val(i.attr('placeholder'));}).on('blur',function(){var i=$(this);if(i.attr('name').match(/-polyfill-field$/))
return;if(i.val()=='')
i.addClass('polyfill-placeholder').val(i.attr('placeholder'));}).on('focus',function(){var i=$(this);if(i.attr('name').match(/-polyfill-field$/))
return;if(i.val()==i.attr('placeholder'))
i.removeClass('polyfill-placeholder').val('');});$this.find('input[type=password]').each(function(){var i=$(this);var x=$($('<div>').append(i.clone()).remove().html().replace(/type="password"/i,'type="text"').replace(/type=password/i,'type=text'));if(i.attr('id')!='')
x.attr('id',i.attr('id')+'-polyfill-field');if(i.attr('name')!='')
x.attr('name',i.attr('name')+'-polyfill-field');x.addClass('polyfill-placeholder').val(x.attr('placeholder')).insertAfter(i);if(i.val()=='')
i.hide();else
x.hide();i.on('blur',function(event){event.preventDefault();var x=i.parent().find('input[name='+i.attr('name')+'-polyfill-field]');if(i.val()==''){i.hide();x.show();}});x.on('focus',function(event){event.preventDefault();var i=x.parent().find('input[name='+x.attr('name').replace('-polyfill-field','')+']');x.hide();i.show().focus();}).on('keypress',function(event){event.preventDefault();x.val('');});});$this.on('submit',function(){$this.find('input[type=text],input[type=password],textarea').each(function(event){var i=$(this);if(i.attr('name').match(/-polyfill-field$/))
i.attr('name','');if(i.val()==i.attr('placeholder')){i.removeClass('polyfill-placeholder');i.val('');}});}).on('reset',function(event){event.preventDefault();$this.find('select').val($('option:first').val());$this.find('input,textarea').each(function(){var i=$(this),x;i.removeClass('polyfill-placeholder');switch(this.type){case'submit':case'reset':break;case'password':i.val(i.attr('defaultValue'));x=i.parent().find('input[name='+i.attr('name')+'-polyfill-field]');if(i.val()==''){i.hide();x.show();}
else{i.show();x.hide();}
break;case'checkbox':case'radio':i.attr('checked',i.attr('defaultValue'));break;case'text':case'textarea':i.val(i.attr('defaultValue'));if(i.val()==''){i.addClass('polyfill-placeholder');i.val(i.attr('placeholder'));}
break;default:i.val(i.attr('defaultValue'));break;}});});return $this;};$.prioritize=function($elements,condition){var key='__prioritize';if(typeof $elements!='jQuery')
$elements=$($elements);$elements.each(function(){var $e=$(this),$p,$parent=$e.parent();if($parent.length==0)
return;if(!$e.data(key)){if(!condition)
return;$p=$e.prev();if($p.length==0)
return;$e.prependTo($parent);$e.data(key,$p);}
else{$p=$e.data(key);$e.insertAfter($p);$e.removeData(key);}});};})(jQuery);(function($){skel.breakpoints({xlarge:'(max-width: 1680px)',large:'(max-width: 1280px)',medium:'(max-width: 980px)',small:'(max-width: 736px)',xsmall:'(max-width: 480px)'});$(function(){var $window=$(window),$body=$('body');$body.addClass('is-loading');$window.on('load',function(){window.setTimeout(function(){$body.removeClass('is-loading');},0);});if(skel.vars.mobile)
$body.addClass('is-touch');$('form').placeholder();skel.on('+medium -medium',function(){$.prioritize('.important\\28 medium\\29',skel.breakpoint('medium').active);});$('.scrolly').scrolly({speed:2000});$('#nav > ul').dropotron({alignment:'right',hideDelay:350});$('<div id="titleBar">'+'<a href="#navPanel" class="toggle"></a>'+'<span class="title">'+$('#logo').html()+'</span>'+'</div>').appendTo($body);$('<div id="navPanel">'+'<nav>'+
$('#nav').navList()+'</nav>'+'</div>').appendTo($body).panel({delay:500,hideOnClick:true,hideOnSwipe:true,resetScroll:true,resetForms:true,side:'left',target:$body,visibleClass:'navPanel-visible'});if(skel.vars.os=='wp'&&skel.vars.osVersion<10)
$('#titleBar, #navPanel, #page-wrapper').css('transition','none');if(skel.vars.browser=='ie'||skel.vars.mobile){$.fn._parallax=function(){return $(this);};}
else{$.fn._parallax=function(){$(this).each(function(){var $this=$(this),on,off;on=function(){$this.css('background-position','center 0px');$window.on('scroll._parallax',function(){var pos=parseInt($window.scrollTop())-parseInt($this.position().top);$this.css('background-position','center '+(pos*-0.15)+'px');});};off=function(){$this.css('background-position','');$window.off('scroll._parallax');};skel.on('change',function(){if(skel.breakpoint('medium').active)
(off)();else
(on)();});});return $(this);};$window.on('load resize',function(){$window.trigger('scroll');});}
var $spotlights=$('.spotlight');$spotlights._parallax().each(function(){var $this=$(this),on,off;on=function(){$this.css('background-image','url("'+$this.find('.image.main > img').attr('src')+'")');if(skel.canUse('transition')){var top,bottom,mode;if($this.hasClass('top')){mode='top';top='-20%';bottom=0;}
else if($this.hasClass('bottom')){mode='bottom-only';top=0;bottom='20%';}
else{mode='middle';top=0;bottom=0;}
$this.scrollex({mode:mode,top:top,bottom:bottom,initialize:function(t){$this.addClass('inactive');},terminate:function(t){$this.removeClass('inactive');},enter:function(t){$this.removeClass('inactive');},});}};off=function(){$this.css('background-image','');if(skel.canUse('transition')){$this.unscrollex();}};skel.on('change',function(){if(skel.breakpoint('medium').active)
(off)();else
(on)();});});var $wrappers=$('.wrapper');$wrappers.each(function(){var $this=$(this),on,off;on=function(){if(skel.canUse('transition')){$this.scrollex({top:250,bottom:0,initialize:function(t){$this.addClass('inactive');},terminate:function(t){$this.removeClass('inactive');},enter:function(t){$this.removeClass('inactive');},});}};off=function(){if(skel.canUse('transition'))
$this.unscrollex();};skel.on('change',function(){if(skel.breakpoint('medium').active)
(off)();else
(on)();});});var $banner=$('#banner');$banner._parallax();});})(jQuery);!(function($){$.fn.unveilEffect=function(callback,threshold){var $w=$(window),th=threshold||0,images=this,loaded,inview,source;this.one('unveil.effect',callback)
function unveil(){inview=images.filter(function(){var $e=$(this),wt=$w.scrollTop(),wb=wt+$w.height(),et=$e.offset().top,eb=et+$e.height();return eb>=wt-th&&et<=wb+th;});loaded=inview.trigger("unveil.effect");images=images.not(loaded);}
$w.scroll(unveil).resize(unveil).load(unveil);return this;};unveilEffectSettings=$.extend({transitionDuration:0.7,transitionEasing:"ease-in-out",selector:'[data-effect]',threshold:100},(typeof(unveilEffectSettings)!='undefined'?unveilEffectSettings:false));$(function(){$.fn.unveilEffect.transition=(function(){var el=document.createElement('bs')
var transEndEventNames={'WebkitTransition':'-webkit-transition','MozTransition':'-moz-transition','OTransition':'-o-transition','transition':'-transition'}
for(var name in transEndEventNames){if(el.style[name]!==undefined){return{css:transEndEventNames[name]}}}})();if(!$.fn.unveilEffect.transition)
return;var animSelector=$(unveilEffectSettings.selector);animSelector.each(function(){var $this=$(this),effectName=$this.data('effect');$this.addClass('effect-'+effectName)[0].offsetWidth;$this.css($.fn.unveilEffect.transition.css,'all '+
unveilEffectSettings.transitionDuration+'s '+
unveilEffectSettings.transitionEasing)}).unveilEffect(function(){$(this).addClass('in')},(-unveilEffectSettings.threshold))})})(window.jQuery);