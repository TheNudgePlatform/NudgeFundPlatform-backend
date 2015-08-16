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
        var textBoxShown = false;
	$(".jqAddMoney").on("click", function(event) {
		event.preventDefault();
                if(!textBoxShown) {
			$(".jqAddMoneyForm").removeClass("hidden");
                        textBoxShown = true;
                } else {
		       var walletAmountElem = $("#walletAmount");
                       var value = parseFloat($("#loanAmount").val());
                       var walletAmount = parseFloat(walletAmountElem.html().substr(1));
                       walletAmount += value;
		       walletAmountElem.html("$"+walletAmount);
                }
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
