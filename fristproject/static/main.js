var parks1= document.getElementById('parks1')
var parks2= document.getElementById('parks2')
var parks3= document.getElementById('parks3')
var parks4= document.getElementById('parks4')
var parks5= document.getElementById('parks5')
var parks6= document.getElementById('parks6')
var parks7= document.getElementById('parks7')
var parks8= document.getElementById('parks8')
var parks9= document.getElementById('parks9')
var parks10= document.getElementById('parks10')


function myfunction(){

if(y[0]==0){
parks1.className = "parked";
parks1.innerHTML="Parking not avaiable <br><br>";
}
else if (y[0]==2) {
parks1.className = "taken";
parks1.innerHTML="Parking is reserved... <br><br>";
}

if(y[1]==0){
parks2.className = "parked";
parks2.innerHTML="Parking not avaiable <br><br>";
}


else if (y[1]==2) {
parks2.className = "taken";
parks2.innerHTML="Parking is reserved... <br><br>";
}

if(y[2]==0){
parks3.className = "parked";
parks3.innerHTML="Parking not avaiable <br><br>";
}

else if (y[2]==2) {
parks3.className = "taken";
parks3.innerHTML="Parking is reserved... <br><br>";
}
if(y[3]==0){
parks4.className = "parked";
parks4.innerHTML="Parking not avaiable <br><br>";
}
else if (y[3]==2) {
parks4.className = "taken";
parks4.innerHTML="Parking is reserved... <br><br>";
}
if(y[4]==0){
parks5.className = "parked";
parks5.innerHTML="Parking not avaiable <br><br>";
}
else if (y[4]==2) {
parks5.className = "taken";
parks5.innerHTML="Parking is reserved... <br><br>";
}
if(y[5]==0){
parks6.className = "parked";
parks6.innerHTML="Parking not avaiable <br><br>";
}
else if (y[5]==2) {
parks6.className = "taken";
parks6.innerHTML="Parking is reserved... <br><br>";
}
if(y[6]==0){
parks7.className = "parked";
parks7.innerHTML="Parking not avaiable <br><br>";
}
else if (y[6]==2) {
parks7.className = "taken";
parks7.innerHTML="Parking is reserved... <br><br>";
}
if(y[7]==0){
parks8.className = "parked";
parks8.innerHTML="Parking not avaiable <br><br>";
}
else if (y[7]==2) {
parks8.className = "taken";
parks8.innerHTML="Parking is reserved... <br><br>";
}
if(y[8]==0){
parks9.className = "parked";
parks9.innerHTML="Parking not avaiable <br><br>";
}
else if (y[8]==2) {
parks9.className = "taken";
parks9.innerHTML="Parking is reserved... <br><br>";
}
if(y[9]==0){
parks10.className = "parked";
parks10.innerHTML="Parking not avaiable <br><br>";
}
else if (y[9]==2) {
parks10.className = "taken";
parks10.innerHTML="Parking is reserved... <br><br>";
}
}
myfunction();

function reserve(x){
	
	var html=document.getElementById(x).innerHTML;
if(html.length<=22){
		if(i==1){
			document.getElementById(past).className="park";
			document.getElementById(past).innerHTML="Parking Avaiable"
		}	
			document.getElementById(x).className="reserve";
			document.getElementById(x).innerHTML="Slot Seleted for reservation"
			document.getElementById('myBtn').className='btn';
			past=x;
			slot=x.substr(5,2);

			i=1;
		
}
}


 function popup(){

    alert("you have sucessfully reserved the Spot");
  }

// function getslot(){
	
// 	document.getElementById('rfidtag').value=slot;
// }


//asdfas
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
 
    document.getElementById('rfidtag').value=slot;
    document.getElementById('spc').value=slot;

}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
} 