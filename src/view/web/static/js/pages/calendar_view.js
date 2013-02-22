$(document).ready(function() {
    $('#closeButton').click(function() { 
        $('#enter_activity_modal').modal('hide'); 
    });

    $('#closeButton_view').click(function() { 
        $('#view_activity_modal').modal('hide'); 
    });

    $('form').submit(function() { 
        $.post("create", $(this).serialize(), function() {
            $('#enter_activity_modal').modal('hide');
                $('#calendar').fullCalendar('refetchEvents');
        });
        return false;
    });

    $('#calendar').fullCalendar({
        header: {
            left:   'prev',
			center: 'title',
			right:  'today, next'
		},

        weekMode:   'variable',

        editable:   false,

        eventColor: "#dd4814",

        dayClick: function(date) {
            $('#enter_activity_modal').modal('show');
            $('#date').attr('value', date.getDate() + "-" + 
                (date.getMonth()+1) + "-" + 
                date.getFullYear());
            $('#modal_title').html("New Activity (" + 
                (date.getMonth()+1) + "/" + 
                date.getDate() + "/" + 
                date.getFullYear() + ")");

            $('#type').attr('value', '');
                $('#distance').attr('value', '');
                $('#duration').attr('value', '');
                $('#max_speed').attr('value', '');
            },

            eventClick: function(event) {
                $('#view_activity_modal').modal('show');

                $('#view_modal_title').html(event.type + " (" + 
                        event.event_date + ")");

                $('#distance_view').html(event.distance + " km");
                $('#duration_view').html(event.duration + " mins");
                $('#max_speed_view').html(event.max_speed + " km/h");
            },

            events: function(start, end, callback) {
                $.ajax({
                    url:        'json',
                    dataType:   'json',
                    data: {
                    start_date: start.toJSON(),
                    end_date:   end.toJSON()
                },
                
                success: function(doc) {
                    var events = [];
                    $(doc.activities).each(function() {
                        events.push({
                            // Full Calendar Dependant JSON:  
                            title:      $(this).attr('type') + "\n" + 
                                        $(this).attr('distance') + " km \n" + 
                                        $(this).attr('duration') + " mins",
                            start:      $(this).attr('date'),
                            end:        $(this).attr('date'),
                            // Event Information:                                    
                            type:       $(this).attr('type'),
                            event_date: $(this).attr('date'),
                            distance:   $(this).attr('distance'),
                            duration:   $(this).attr('duration'),
                            max_speed:  $(this).attr('max_speed')
                        });
                    });
                    callback(events);
                }
            });
        }
    })
});
