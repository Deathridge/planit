// Refresh the Table every 5 seconds
setInterval(function(){
    $.ajax({    
       url: "refresh",
       type: "GET",
          success: function(data) {
          $('#flights').html(data);
          }
    });
}, 5000)