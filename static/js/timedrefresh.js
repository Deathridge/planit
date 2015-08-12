// Refresh the Table every 5 seconds
setInterval(function(){
    $.ajax({
    	url: 'r',
    	success: function(data){
    		$('.flights').replaceWith(data)
    	}
    })
    
}, 20000)