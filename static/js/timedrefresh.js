// Refresh the Table every 500 millseconds
setInterval(function(){
    $.ajax({
    	url: 'flights/r',
    	success: function(data){
    		$('.flights').replaceWith(data)
    	}
    })
    
}, 500)

$(document).ready(function() {
        $('#flightform').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                    //$('#flight-form').html(response); // update the DIV
                }
            });
            return false;
        });
    });