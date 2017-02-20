// fundtion to display single digit seconds and minuts as two digits
function display_time(n){
    return n > 9 ? "" + n: "0" + n;
}

$(document).ready(function() {

  var working = true;

  var break_time = $("#break_time").html();
  var work_time = $("#work_time").html();

  var started = false;

  var completed = 0;
  var progress = 0;

  // use to calculate numbers to go into timer box
  var mins = 0;
  var seconds = 0;

  $(function() {
    if (started) {
      setInterval(updateTime, 1000);
    }
   });

  // start timer
  $("#start_timer").click(function() {
    working = true;
    if (!started) {
      setInterval(updateTime,1000);
      started = true;
    }

    completed = 0;
    progress = 0;

    // use to calculate numbers to go into timer box
    mins = 0;
    seconds = 0;


  })

  // function to update the timer and apply changes to the progress bar
  function updateTime() {

    // code to update progress bars and clock
    if (working) {
      completed += 1;
      if (completed > work_time*60) {
        working = false;
        progress = 0;
        completed = 0;
      }
      progress = (completed / parseFloat(work_time)) * (100/60);

      // calculate minutes and seconds to display
      var total_seconds = work_time*60;
      var time_remaining = total_seconds - completed;
      mins = Math.floor(time_remaining/60);
      seconds = time_remaining - mins*60;


      $("#time_left").html(mins + ":" + display_time(seconds))
      $("#work_progress").attr('aria-valuenow', progress).css('width', progress + "%");

    }
    else {
      completed += 1;
      if (completed > break_time*60) {
        working = true;
        progress = 0;
        completed = 0;
      }
      progress = (completed / parseFloat(break_time))*(100/60);

      // calculate minutes and seconds to display
      var total_seconds = break_time*60;
      var time_remaining = total_seconds - completed;
      mins = Math.floor(time_remaining/60);
      seconds = time_remaining - mins*60;


      $("#time_left").html(mins + ":" + display_time(seconds))
      $("#break_progress").attr('aria-valuenow', progress).css('width', progress + "%");

    }
  }

  // subtract time from break
  $("#subtract_break").click(function() {
    if (break_time > 1) {
      break_time = parseInt(break_time) - 1;
      $("#break_time").html(break_time);
    }
  });

  // add time to break
  $("#add_break").click(function() {
    break_time = parseInt(break_time) + 1;
    $("#break_time").html(break_time);
  });

  // subtract time from work
  $("#subtract_work").click(function() {
    if (work_time > 1) {
      work_time = parseInt(work_time) - 1;
      $("#work_time").html(work_time);
    }
  });

  // add time to work
  $("#add_work").click(function() {
    work_time = parseInt(work_time) + 1;
    $("#work_time").html(work_time);
  });

})
