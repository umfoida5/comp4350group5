function Activities(){

    this.controls = function() {
        
        $('#enterButton').click(function() {
            $('#enter_activity_modal').modal('show');
            $('#type').attr('value', 'Run');
            $('#distance').attr('value', '');
            $('#duration').attr('value', '');
            $('#max_speed').attr('value', '');
            $('#dateInput').datepicker('setValue', new Date());
        });

        $('#closeButton').click(function() { 
            $('#enter_activity_modal').modal('hide'); 
        });

        $('#closeButton_view').click(function() { 
            $('#view_activity_modal').modal('hide'); 
        });

        
    }
    
    $('#dateInput').datepicker().on('changeDate', function(){
        $(this).datepicker('hide');
    });

    this.athleteTable = function(){
      var athleteTable = $('#athleteTable').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sPaginationType": "bootstrap",
        "sAjaxSource": "update_datatable",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "type", "sWidth": '25%' },
          { "mData": "date", "sWidth": '30%', "bSearchable": false },
          { "mData": "duration", "sWidth": '15%', "bSearchable": false },
          { "mData": "distance", "sWidth": '15%', "bSearchable": false },
          { "mData": "max_speed", "sWidth": '15%', "bSearchable": false }
        ]} );

        $('form').submit(function() { 
            $.post("create", $(this).serialize(), function() {
                $('#enter_activity_modal').modal('hide');
                $('#calendar').fullCalendar('refetchEvents');
                athleteTable.fnDraw();
            });
            return false;
        });
    }

    this.ajax_calendar = function() {
        var xhr = $('#calendar').fullCalendar({
            header: {
                left:   'title',
		        center: '',
		        right:  'prev, next'
	        },

            weekMode:   'variable',

            editable:   false,

            eventColor: "#dd4814",

            dayClick: function(date) {
                $('#enter_activity_modal').modal('show');
                $('#dateInput').datepicker('setValue', new Date(date.getFullYear(), date.getMonth(), date.getDate()));
                $('#modal_title').html("New Activity");
                $('#type').attr('value', 'Run');
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
                    url:        '../activities/json',
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
        return xhr;
    }
}

var activity = new Activities();
