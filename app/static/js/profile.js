$(document).ready(function() {

			$("#L4").click(function() {
				$("#hangboardTable").toggle();
			});



			$.getJSON("/data/hangboard", function(data) {

				data.forEach(function(item) {

					$('#board').append('<p> ' + item.board + '</p>');
					$('#hold_used').append('<p> ' + item.holds_used + '</p>');
					$('#arm_used').append('<p> ' + item.arm_used + '</p>');
					$('#reps').append('<p> ' + item.reps + '</p>');
					$('#rest').append('<p> ' + item.resttime + '</p>');
					$('#date').append('<p> ' + item.timestamp.substring(0, 17) + '</p>');
					$('#weight').append('<p>' + item.weight_kg + '</p>');


				});


			});



			$(document).ready(function() {

				$("#L3").click(function() {
					$("#routesTable").toggle();
				});


				$.getJSON("/data/routes", function(data) {

					data.forEach(function(item) {

						$('#angle').append('<p> ' + item.angle + '</p>');
						$('#grade').append('<p> ' + item.grade + '</p>');
						$('#height').append('<p> ' + item.height + '</p>');
						$('#intensity').append('<p> ' + item.intensity + '</p>');
						$('#style').append('<p> ' + item.style + '</p>');
						$('#dateroutes').append('<p> ' + item.timestamp.substring(0, 17) + '</p>');
						$('#venue').append('<p>' + item.venue + '</p>');
						$('#duration').append('<p>' + item.werktime + '</p>');

					});

				});


			});

			$(document).ready(function() {

				$("#L2").click(function() {
					$("#kampusTable").toggle();
				});


				$.getJSON("/data/kampus", function(data) {

					data.forEach(function(item) {

						$('#kampuslog').append('<p> ' + item.kampuslog + '</p>');
						
						$('#datekampus').append('<p> ' + item.timestamp.substring(0, 17) + '</p>');
					
						

					});

				});


			});

			$(document).ready(function() {

				$("#L1").click(function() {
					$("#circuitsTable").toggle();
				});


				$.getJSON("/data/circuits", function(data) {

					data.forEach(function(item) {

						$('#circuitsgrade').append('<p> ' + item.grade + '</p>');						
						$('#numberofmoves').append('<p> ' + item.numberofmoves + '</p>');
						$('#circuitintensity').append('<p> ' + item.intensity + '</p>');
						$('#datecircuits').append('<p> ' + item.timestamp.substring(0, 17) + '</p>');
						$('#circuitduration').append('<p>' + item.werktime + '</p>');
						$('#circuitcomments').append('<p>' + item.comments + '</p>');


					});

				});


			});


			$(document).ready(function() {

				$("#L0").click(function() {
					$("#blocTable").toggle();
				});


				$.getJSON("/data/blocs", function(data) {

					data.forEach(function(item) {

						$('#blocangle').append('<p> ' + item.angle + '</p>');
						$('#blocgrade').append('<p> ' + item.grade + '</p>');
						$('#blocintensity').append('<p> ' + item.intensity + '</p>');
						$('#datebloc').append('<p> ' + item.timestamp.substring(0, 17) + '</p>');
						$('#blocduration').append('<p>' + item.werktime + '</p>');
						$('#bloccomments').append('<p>' + item.comments + '</p>');
						$('#blocvenue').append('<p>' + item.venue + '</p>');
						$('#blocstyle').append('<p>' + item.style + '</p>');


					});

				});


			});








});