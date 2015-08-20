
    $(document).ready(function() {
    	//page is ready resize calendar
    	viewScreenSize();
    	if (thisScreenWidth < 601) $('#calendar').fullCalendar('changeView', 'agendaDay');
    	else $('#calendar').fullCalendar('changeView', 'month');
    // page is now ready, initialize the calendar...

    	var calendar = $('#calendar').fullCalendar(
    	{
        	defaultView: 'agendaWeek',    		
    		selectable: true,
			selectHelper: true,
			height: 500,
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
							allDay: allDay
						},
						true // make the event "stick"
					);
				}
				calendar.fullCalendar('unselect');

				
			},

			editable: true,	


    	})

    	$('#calendar').addTouch();    	
    	
    	
	});   	


$(window).bind('resize', function () {
	viewScreenSize();
    if (thisScreenWidth < 601) $('#calendar').fullCalendar('changeView', 'agendaDay');
    else $('#calendar').fullCalendar('changeView', 'month');
});
