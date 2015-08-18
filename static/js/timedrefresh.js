// Refresh the Table every 500 millseconds
setInterval(function(){
    $.ajax({
    	url: 'flights/r',
    	success: function(data){
    		$('.flights').replaceWith(data)
    	}
    })
    
}, 500)

function flightSubmit(){
    var dataString = '&flightcode=' + $('input[id=flightcode]').val() +
                     '&departuredate=' + $('input[id=departuredate]').val() +
    $.ajax({
        type: "POST",
        url: "",
        data: dataString,
        success: function(data) {
            alert(data);
        }   
     }); 
     return false;   
}