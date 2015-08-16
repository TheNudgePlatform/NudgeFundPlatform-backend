$(function () {
	/* on scroll show top nav */
    // $(window).on("scroll", function() {
    //     var bodyScrollTop = $("body").scrollTop();
    //     if(bodyScrollTop > 500) {
    //         $(".jsTopNav").addClass("show-bg");
    //     } else {
    //         $(".jsTopNav").removeClass("show-bg");
    //     }
    // });

	/* User menu dropdown */
	$(".jsUserName").on("click", function(event) {
		$(".jsUserDD").toggleClass("open");
	});
	$(document).on("click", function(event) {
		var target = $(event.target);
		window.target = target;
		if(!target.hasClass("jsUserName")) {
			$(".jsUserDD").removeClass("open");
		}
	});
});
