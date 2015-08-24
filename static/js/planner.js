
    $(document).ready(function() {
    	//page is ready resize calendar
    	
    // page is now ready, initialize the calendar...

    	var calendar = $('#calendar').fullCalendar(
    	{
        	defaultView: 'agendaWeek',    		
    		selectable: true,
			selectHelper: true,
			height: 500,
			

        	// any other sources...

    		
				/*
					when user select timeslot this option code will execute.
					It has three arguments. Start,end and allDay.
					Start means starting time of event.
					End means ending time of event.
					allDay means if events is for entire day or not.
				*/
			select: function(start, end, allDay)
			{
					/*
						after selection user will be promted for enter title for event.
					*/
				var title = prompt('Event Title:');
				var description = prompt('Event description:');
				
					/*
						if title is enterd calendar will add title and event into fullCalendar.
					*/
				if (title)
				{
					calendar.fullCalendar('renderEvent',
						{
							title: title,
							start: start,
							end: end,
							description,
							
						},
						true // make the event "stick"
					);
				}
				calendar.fullCalendar('unselect');

				
			},

			

			eventSources: [{
				url:'/planner/json'
			}],
			
			editable: true,	

			eventRender: function(event, element) {
    		    element.qtip({
    		    content: event.description ,    
    		    position: {	
    		    my: 'bottom left',
        		// Position my top left...
        		at: 'top right',
        		// at the bottom right of...
        		target: 'mouse'
        		}   		    
            	        	
        		});
    		}

    	})

    	$('#calendar').addTouch();    	
    	viewScreenSize();
    	if (thisScreenWidth < 601) $('#calendar').fullCalendar('changeView', 'agendaDay');
    	else $('#calendar').fullCalendar('changeView', 'agendaWeek');
    	
	});   	


$(window).bind('resize', function () {
	viewScreenSize();
    if (thisScreenWidth < 601) $('#calendar').fullCalendar('changeView', 'agendaDay');
    else $('#calendar').fullCalendar('changeView', 'agendaWeek');
});
