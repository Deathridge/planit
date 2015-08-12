// Refresh the Table every 5 seconds
setInterval(function(){
    $.ajax({
    	url: '/r/',
    	success: function(data){
    		$('#flights').load(data)
    	}
    })
    
}, 5000)