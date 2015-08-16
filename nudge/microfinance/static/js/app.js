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

	$(".jqAddMoney").on("click", function(event) {
		event.preventDefault();
		$(".jqAddMoneyForm").removeClass("hidden");
	});

	/* User profile page nav bar handling */
	var navLiElem = $(".jsUserNav li");
	navLiElem.on("click", function(event) {
		var nav = $(this).data("nav");
		navLiElem.removeClass("active");
		$(this).addClass("active");
		$(".jsUserPages > .row").removeClass("show");
		$("#" + nav).addClass("show");
	});
});
