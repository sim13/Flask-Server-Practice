//JAVASCRIPT Y'ALL


//P.S.--> Don't name variables with just random numbers, make them more semantic
//P.P.S.--> Gobal variable are bad, they pollute the namespace. Use a global object to store all data inside it.
var menu = document.getElementById("menu");
var overlay = document.getElementById("overlay");
var heading = document.getElementById("heading");
var button = document.getElementById("proceed-button");
var quote = document.getElementById("splash-quote");
var content = document.getElementById("main-content");
var element4 = document.getElementById("wrap2.animate"); //<-- what is this??


//___##_CLICK_HANDLERS_##___//
//click events and the functions triggered by them
//- LIST :-
//- # Proceed button click (#butt)
//- # Cross button to hide overlay (#cross)

//# the proceed button reveals the main page
document.getElementById("proceed-button").addEventListener('click', function() {

	//--First animate out the existing heading and the proceed button
	overlay.style.opacity 	 = 0.8;
	heading.className 		+= " animate-out";
	button.className 		+= " animate-out";

	//--Then animate in the top menu for the nav
	menu.className 			+= " animate-in";
	quote.className 		+= " animate-in";
	//-TODO
	
	//--Finally, the main body for the content
	content.className 		+= " animate-in-from-below";
	//-TODO
})

//#
// document.getElementById("cross").addEventListener('click', function() { 
	
// 	if(cross.className == "wrap") {
// 		cross.className = "";
// 		wrap2.className = "";
// 		element2.style.backgroundColor = "black";
// 		element2.style.opacity = 0.99;
// 	} else {
// 		cross.className ="";
// 	} 
// })



// var elems = document.getElementsByClassName("item");

// for (i=0 ; i<6 ; i++) {
// 	elems[i].onclick= function () {
// 		if (wrap2.className == "") {   
// 			wrap2.className = "animate";
// 			cross.className = "wrap";
// 		}
// 	}

// 	document.getElementById("wrap2").innerHTML = "<p class = 'text' >About Me : My name is Simrin</p> ";
// 	console.log(document.getElementById("wrap2").innerHTML);
// }