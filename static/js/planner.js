
    $(document).ready(function() {

    // page is now ready, initialize the calendar...
    	eventRender: function(event, element) {
            $(element).addTouch();
        }
    	var calendar = $('#calendar').fullCalendar(
    	{
        	defaultView: 'agendaWeek',
    		weekMode: 'liquid',
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

    	
	});   	
