var timer = document.getElementById("timer");
var start = document.getElementById("start");
var pause = document.getElementById("pause");
var resume = document.getElementById("resume");
var id;
// var value = document.getElementById("restvalue").value;
var value = 5

function startTimer(m, s) {
    timer.textContent = m + ":" + s;
    if (s == 0) {
        if (m == 0) {
            return;
        } else if (m != 0) {
            m = m - 1;
            s = 60;
        }
    }

    s = s - 1;
    id = setTimeout(function () {
        startTimer(m, s)
    }, 1000);
}

function pauseTimer() {
    value = timer.textContent;
    clearTimeout(id);
}

function resumeTimer() {
    var t = value.split(":");

    startTimer(parseInt(t[0], 10), parseInt(t[1], 10));
}

start.addEventListener("click", function () {
    startTimer(value, 0);
}, false);

pause.addEventListener("click", pauseTimer, false);

resume.addEventListener("click", resumeTimer, false);