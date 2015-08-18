// Refresh the Table every 500 millseconds
setInterval(function(){
    $.ajax({
    	url: 'flights/r',
    	success: function(data){
    		$('.flights').replaceWith(data)
    	}
    })
    
}, 500)

$('#form').submit(function(e){
    $.post('', $(this).serialize(), function(data){                
    });
    e.preventDefault();
});