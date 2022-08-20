function upload() {
	let image = document.getElementById('image');
	console.log("Upload cai ne")
	$.ajax({
		url: "http://localhost:5000/test",
		dataType: "json",
		type:"POST",
		data:'Payam',
    	success: function(data){
        	console.log(data);
    	}
	});
}

alert("cay vc")