// Refresh the Table every 5 seconds
setInterval(function(){
    $.ajax({    
       url: "/"
    });
}, 5000)