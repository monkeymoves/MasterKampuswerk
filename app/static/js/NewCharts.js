var hangsessions = $.getJSON("/data/hangboard", function(data) {
    hangsessions = data.length;
});

var lastweekofhangsessions = $.getJSON("/data/hangboard/7days", function(data) {
    lastweekofhangsessions = data.length;
});


var routesessions = $.getJSON("/data/routes", function(data) {
    routesessions = data.length;
});

var lastweekofroutesessions = $.getJSON("/data/routes/7days", function(data) {
    lastweekofroutesessions = data.length;
});


var kampussessions = $.getJSON("/data/kampus", function(data) {
    kampussessions = data.length;
});

var lastweekofkampussessions = $.getJSON("/data/kampus/7days", function(data) {
    lastweekofkampussessions = data.length;
});

var circuitsessions = $.getJSON("/data/circuits", function(data) {
    circuitsessions = data.length;
});

var lastweekofcircuitsessions = $.getJSON("/data/circuits/7days", function(data) {
    lastweekofcircuitsessions = data.length;
});

var blocsessions = $.getJSON("/data/blocs", function(data) {
    blocsessions = data.length;
});

var lastweekofblocsessions = $.getJSON("/data/blocs/7days", function(data) {
    lastweekofblocsessions = data.length;
});


$("#chart_totals").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Hangboard", "Routes", "Kampus", "Circuits", "Blocs"],

            datasets: [{
                    label: 'All Time Total Sessions',
                    data: [hangsessions, routesessions, kampussessions, circuitsessions, blocsessions],
                    backgroundColor: [

                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 64, 0.6)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


$("#L0chart").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Hangboard", "Routes", "Kampus", "Circuits", "Blocs"],

            datasets: [{
                    label: 'Total Sessions Last Week',
                    data: [lastweekofhangsessions, lastweekofroutesessions, lastweekofkampussessions, lastweekofcircuitsessions, lastweekofblocsessions],
                    backgroundColor: [

                      
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 64, 0.6)'
                    ],
                    borderColor: [
                      
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


$("#L1chart").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Last week", "All time"],

            datasets: [{
                    label: 'Circuits - Number of Sessions',
                    data: [lastweekofcircuitsessions, circuitsessions],
                    backgroundColor: [

                      
                      
                        'rgba(255, 159, 64, .6)',
                        'rgba(255, 159, 64, .6)'
                    ],
                    borderColor: [
                      
                     
                        'rgba(255, 159, 64, .6)',
                        'rgba(255, 159, 64, .6)'
                    ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


$("#L2chart").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [ "Last week", "All time"],

            datasets: [{
                    label: 'Kampus - Number of Sessions',
                    data: [lastweekofkampussessions, kampussessions ],
                    backgroundColor: [

                      
                        'rgba(0, 159, 218, 0.6)',
                        'rgba(0, 159, 218, 0.6)'
                
                    ],
                    borderColor: [
                         'rgba(0, 159, 218, 0.6)',
                        'rgba(0, 159, 218, 0.6)'
                    ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


$("#L3chart").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [ "Last week", "All time"],

            datasets: [{
                    label: 'Routes - Number of Sessions ',
                    data: [ lastweekofroutesessions, routesessions],
                    backgroundColor: [

                      
                       'rgba(0, 142, 109, .6)',
                        'rgba(0, 142, 109, .6)',
                     
                    ],
                    borderColor: [
                      
                      'rgba(0, 142, 109, .6)',
                        'rgba(0, 142, 109, .6)',
                    
                    ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


$("#L4chart").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Last week", "All time"],

            datasets: [{
                    label: 'Hangboard - Number of Sessions',
                    data: [lastweekofhangsessions, hangsessions],
                    backgroundColor: [

                      
                       
                        'rgba(  0, 66, 50, .6)',
                        'rgba(  0, 66, 50, .6)',
                    ],
                    borderColor: [
                      
                       
                        'rgba(  0, 66, 50, .6)',
                        'rgba(  0, 66, 50, .6)',                   ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


$("#L5chart").click(function() {



    var ctx = document.getElementById("ChartT2");
    var ChartT2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Last week", "All time"],

            datasets: [{
                    label: 'Blocs - Number of Sessions',
                    data: [lastweekofblocsessions, blocsessions],
                    backgroundColor: [

                        'rgba(255, 99, 132, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                      
                    ],
                    borderColor: [
                      
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                    ],
                    borderWidth: 1
                },


            ]
        },
        options: {
            legendPosition: 'right',
            color: 'blue',

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});

