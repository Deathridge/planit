

$(document).ready(function() {
        $('#flightform').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                	$.ajax({
                        type: "GET",
                        url: '/flights'
                        success: function(data){
                            $('.message-alert').replaceWith(data)
                        }
                    }
                    $.ajax({
    					url: 'refresh',
    					success: function(data){
    						$('.flights').replaceWith(data)
                            
    					}
    				})

                }
            });
            return false;
        });
    });