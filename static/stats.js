google.load("visualization", "1", {packages:["corechart", 'annotatedtimeline']});

var results;

$(document).ready(function(){
  console.log("document load");
  resume(20000);
  $("#refresh").click(function(){
    var max = $("#max").val();
    resume(max);
  });
  
  $(".sensor").click(function(){
    drawChart(results);
  });
  
});

function resume(max){
    
    console.log("Data requests, max "+max);
    $.ajax({
    url: "sensor/all?max="+max,
    dataType: "json",
    success: function (json) {
        results= json;
        drawChart(json);
      }
    });
}

function drawChart(jsonResume) {

    console.log("Loading chart");
    var results =  [],
        lightEnabled = $("#light").prop("checked"),
        tempEnabled = $("#temperature").prop("checked"),
        humEnabled = $("#humidity").prop("checked");
    results[0] =  ["Date"];    
 
    //dynamic table
    if (lightEnabled) results[0][results[0].length] = "Light";
    if (tempEnabled) results[0][results[0].length] = "Temperature";
    if (humEnabled) results[0][results[0].length] = "Humidity";
    
    console.log("Enabled sensors: light "+lightEnabled+ ", temp "+tempEnabled + " humidity "+ humEnabled);
  
    
    for (i in jsonResume.results){
        var stat = jsonResume.results[i],
            index = parseInt(i)+1;
        
        results[index] = [new Date(stat.datetime)];
            
        if (lightEnabled) results[index][results[index].length] = stat.light;
        if (tempEnabled) results[index][results[index].length] = stat.temperature;
        if (humEnabled) results[index][results[index].length] = stat.humidity;
    }

    var data = google.visualization.arrayToDataTable(results);

    var options = {
      title: 'Sensors'
    };
    
    var chart = new google.visualization.AnnotatedTimeLine(document.getElementById('chart_div'));
    chart.draw(data, options);
}