$(document).ready(function () {
	
	function TimerStart() {
		var hangTime  = parseInt($("#hangtime select").val());
		var restTime  = parseInt($("#resttime input").val());
		var body = document.getElementsByTagName('body')[0]
		var totalReps = parseInt($("#reps select").val());  
		var totalSets = parseInt($("#sets select").val());  
		var setRest	= parseInt($("#setrest input").val());
		var reverseReps = totalReps; 
		var prepTime = 13;
		var timer = document.getElementById('Timer');
		var TimerInstructions = document.getElementById("TimerInstructions");
		console.log( hangTime, restTime, totalReps, prepTime, totalSets, setRest );
		var timeout
		  
		$("#PicHangboard").hide();
		$("#userName").hide();
		$("#Timer").show();
		$("#TimerInstructions").show();


		 // speak to robbie re implementing sets & rest (needed for predefined coash set workout)
		
		
		// function setCheck(setrest, totalSets){
		// 	if (totalSets > 1) {
		// 		countdown(setRest, hang)
		// 	}


		// };


		function countDown(x, nextStep, y) {

			if (totalReps < 0){
				$("#Timer").hide();
				$("#TimerInstructions").hide();
				$("#PicHangboard").show();
				$("#userName").show();
				$("#userName").html("Data logged!");
				body.style.background = '#ffffff';
				return 

			} else if (x <= 0) {
				nextStep();
				
				return
			};

			timer.innerHTML = x;
			timeout = window.setTimeout(function() {
			countDown(x-1, nextStep);
			}, 1000);
		};

		function startWorkout(){
			body.style.background = '#3498db';
			TimerInstructions.innerHTML ="PREPARE";

			countDown(prepTime, hang)
		};

		function rest () {
			body.style.background = "#18bc9c"; 
			TimerInstructions.innerHTML ="REST";

			countDown(restTime, hang);

		};

		function hang () {
			body.style.background = "#e74c3c"
			changeOrder = reverseReps - totalReps + 1
			TimerInstructions.innerHTML ="HANG "+ changeOrder;
			totalReps =totalReps-1;
			

			countDown(hangTime, rest, totalReps);


		};


		startWorkout(); 
			
		


	}

	$("#BtnSubmit").on("click", function(e) {
		e.preventDefault();
		$("body").scrollTop(0);

		var data = $("form").serialize();
		$.ajax({
			url:"/hangboard",
			data: data,
			method: "POST"
		}).then(function (data, status) {
			//success
			console.log("success ",data);
			//some code to start timer here. call new function
			TimerStart();
		}, function (error) {
			//failure
			console.log("error ", error);
		})
	});
});

