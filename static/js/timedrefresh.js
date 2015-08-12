// Refresh the Table every 5 seconds
setInterval(function(){
    $('#flights').load("/r");
    
}, 5000)