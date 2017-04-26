$(document).ready(function() {
	$(".candidate").click(function() {
		console.log($(this).find("input[type='radio']").prop("checked"));
		if ($(this).find("input[type='radio']").prop("checked") == false) {
			$(this).parent().find(".candidate img").css({"border": "0px", "filter": "grayscale(100%)"});
			$(this).parent().find(".candidate p").css("font-weight", "normal");

			$(this).find("p").css("font-weight", "bold");
			$(this).find("img").css({"border": "5px solid green", "filter": "grayscale(0%)"});
			$(this).find("input[type='radio']").prop("checked", true);
		}
		else {
			$(this).parent().find(".candidate img").css({"border": "0px", "filter": "grayscale(0%)"});
			$(this).find("p").css("font-weight", "normal");
			$(this).find("input[type='radio']").prop("checked", false);
		}


		totalVote = $("#vote").serializeArray().length - 1; // CSRF code
		console.log(totalVote);
		if (totalVote == 7) {
			$("button").removeAttr("disabled");		
		}
		else {		
			$("button").attr("disabled", "disabled");	
		}	
	})
});