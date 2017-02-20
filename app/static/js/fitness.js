var welcome = document.getElementById('welcome')
var clock = document.getElementById('counter')
var body = document.getElementsByTagName('body')[0]
var description = document.getElementById('description')
var controls = document.getElementById('controls')
//lukes added prep time
// var exercises = ['Jumping Jacks', 'Wall Sit', 'Push-ups', 'Sit-ups','Step-ups', 'Squats', 'Tricep Dips', 'Plank', 'High Knees', 'Lunges', 'Push-ups and Rotation', 'Side Plank']


var exercises = []

function repsArray(i) {
    while (i > 0){
    exercises.push(i)
    i = i-1}
}

repsArray(exerciseReps)

var skip
var current
var timeout
var beep = new Audio("beep.wav")


var counter = document.getElementById('counter')

function countDown(i, nextAction){
  if (i <= 0 || skip) {
    skip = false
    //beep.currentTime = 0
    //beep.play()
    nextAction()
    return
  }
  counter.innerHTML = i
  timeout = window.setTimeout(function(){
    countDown(i-1,nextAction)
  },1000)
}

function reset(){
  welcome.style.display = 'block'
  counter.style.display = 'none'
  description.style.display = 'none'
  controls.style.display = 'none'
  body.style.background = '#3498db'
  skip = true
  current = 0
}


function startWorkout(){
  description.style.display = 'block'
  welcome.style.display = 'none'
  counter.style.display = 'block'
  controls.style.display = 'block'
  current = 0
  skip = false
  prep()
}

function nextWorkout(){
  if (!exercises[current]) { reset(); return }
  body.style.background = "#e74c3c"
  description.innerHTML = "Hang " + exercises[current]
  countDown(workInterval, rest)
  current++
}

function rest(){
  if (!exercises[current]) { callSets (); return }
  body.style.background = "#3498db"
  description.innerHTML = "Rest"
  countDown(restInterval, nextWorkout)
}

function callSets(){
    body.style.background = "#3498db"
    description.innerHTML = "Set Rest"

    current = 0
    sets = sets-1
    console.log(sets)
    countDown(setrest, prep)

    if (sets === 0){
    window.location = "http://www.kampuswerk.com";
    $('#myModal').modal('show');

    window.alert("stay strong")
    reset()
    }

}

function prep() {
    if (!exercises[current]) { reset(); return }
    body.style.background = "#2C3E50"
    description.innerHTML = "Prepare for Set"
    countDown(prepInterval, nextWorkout)
}
start.addEventListener('click',startWorkout)
document.getElementById('skip').addEventListener('click', function(){ skip = true })
document.getElementById('reset').addEventListener('click', function(){ current = null; skip = true })
