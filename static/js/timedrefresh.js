

$(document).ready(function() {
        $('#flightform').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                	
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

function loadplanner(){
     $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: '/planner', // the file to call
                success: function(response) { // on success..
                    
                    $.ajax({
                        url: '/planner',
                        success: function(data){
                            var f = document.getElementById('flights-form');
                            f.parentNode.removeChild(f);
                            var t = document.getElementById('flights-table');
                            t.parentNode.removeChild(t);

                            var p = data;
                            var planner = document.createElement("DIV");
                            planner.replaceWith(p);

                            
                        }
                    })

                }
            });
            return false;
}