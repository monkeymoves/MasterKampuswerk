 $(function() {
    $("#L1").click(function(){
    	addToSeq(document.getElementById('L1').value)
      document.getElementById("p1").innerHTML = Seq;
    }); 
    
     $("#L2").click(function(){
      addToSeq(document.getElementById('L2').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
    
      $("#L3").click(function(){
      addToSeq(document.getElementById('L3').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L4").click(function(){
      addToSeq(document.getElementById('L4').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L5").click(function(){
      addToSeq(document.getElementById('L5').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L6").click(function(){
      addToSeq(document.getElementById('L6').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L7").click(function(){
      addToSeq(document.getElementById('L7').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L8").click(function(){
      addToSeq(document.getElementById('L8').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L9").click(function(){
      addToSeq(document.getElementById('L9').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#L10").click(function(){
      addToSeq(document.getElementById('L10').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R1").click(function(){
      addToSeq(document.getElementById('R1').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R2").click(function(){
      addToSeq(document.getElementById('R2').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R3").click(function(){
      addToSeq(document.getElementById('R3').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R4").click(function(){
      addToSeq(document.getElementById('R4').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R5").click(function(){
      addToSeq(document.getElementById('R5').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R6").click(function(){
      addToSeq(document.getElementById('R6').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R7").click(function(){
      addToSeq(document.getElementById('R7').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R8").click(function(){
      addToSeq(document.getElementById('R8').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R9").click(function(){
      addToSeq(document.getElementById('R9').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
      $("#R10").click(function(){
      addToSeq(document.getElementById('R10').value)
    	document.getElementById("p1").innerHTML = Seq;
    }); 
    
    
    
  
    
     $("#undo").click(function(){
     removeSeq()
     document.getElementById("p1").innerHTML = Seq;
    }); 
    
    $("#submit").click(function(){
      //enter code to send to server/DB  but for now update msg
        var kampuslog = SeqToString(Seq)
        Seq = [];
       // alert(kampuslog)
        
      document.getElementById("p1").innerHTML = "Kampuswerk logged!";
      $.post( "/kampus", {
         kampuslog 
      });
      
      
    }); 
  
    
});





var Seq = [];

function addToSeq (value) {
  Seq.push(value);
}

function removeSeq () {
  Seq.pop();
}

function SeqToString () {
  var string = "";
  for (var i = 0; i < Seq.length; i ++) {
    string += Seq[i] + ",";
  }
  return string;



}