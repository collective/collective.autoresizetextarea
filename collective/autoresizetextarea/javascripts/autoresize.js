jq(document).ready(function() {
	jq('textarea#form-widgets-text').autoResize({
	    // On resize:
	    onResize : function() {
	        jq(this).css({opacity:0.8});
	    },
	    // After resize:
	    animateCallback : function() {
	        jq(this).css({opacity:1});
	    },
	    // Quite slow animation:
	    animateDuration : 300,
	    // More extra space:
	    extraSpace : 40
	});
 });