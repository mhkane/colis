function setStyle(cssText) {
    var sheet = document.createElement('style');
    sheet.type = 'text/css';
    /* Optional */ window.customSheet = sheet;
    (document.head || document.getElementsByTagName('head')[0]).appendChild(sheet);
    return (setStyle = function(cssText, node) {
        if(!node || node.parentNode !== sheet)
            return sheet.appendChild(document.createTextNode(cssText));
        node.nodeValue = cssText;
        return node;
    })(cssText);
};
var previousScroll = 0;
var headerOrgOffset = $('#banner').height();
var colorCss = setStyle('body.landing #header{}') ;
$(window).scroll(function () {
    var currentScroll = $(this).scrollTop();
	if ($(window).width() > 982) {
		if (currentScroll > headerOrgOffset) {
			if (currentScroll > previousScroll) {
				$('#header').hide('slow');
				setStyle('body.landing #header{}', colorCss);
			} else {
				
				colorCss = setStyle('body.landing #header{background-color:#fff; position:fixed; height:100px} body.landing #header a{color:#e81} body.landing #header #nav{top:25%;} ', colorCss);
				$('#header').show('slow')
			};
		} else {
			
			colorCss = setStyle('body.landing #header{}', colorCss);
			$('#header').show('fast')
		}        
    };
    previousScroll = currentScroll;
});