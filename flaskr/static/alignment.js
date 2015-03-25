fs = require('fs');
 
function readDataFiles(file1, file2) {	
	var line1 = fs.readFileSync(file1, 'utf-8').split('\n')[1];
	var line2 = fs.readFileSync(file2, 'utf-8').split('\n')[1];
 
	return [line1, line2];
}
 
function splitArray(line) {
	return line.split("");
}
 
var data = readDataFiles('mel.txt', 'psd.txt');	//read files get DNA data as strings in array [0]-1st string [1]-2nd string
 
var array1 = splitArray(data[0]),	//splits the string into array containing all the tags
	array2 = splitArray(data[1]);

	function createAlignmentFile(file1){
    fs.writeFile("~/swahal2/Desktop/align.txt", "yo" , function(err){
     if(err)
     {
      console.log(err);
     }
     else {
     	console.log("\n It worked");

    }

	})
};
