// Refresh the Table every 5 seconds
setInterval(function(){
    $.ajax({    
       url: '{% url "flights-detail" %}',
          success: function(data) {
          $('#flights').html(data);
          }
    });
}, 5000)