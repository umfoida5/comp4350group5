function Events() {
    this.controls = function() {
      $('#enterButton').click(function() {
        $('#enter_event_modal').modal('show');
        $('#date').attr('value', '');
        $('#location').attr('value', '');
        $('#distance').attr('value', '');
        $('#description').attr('value', '');
      });
      
      $('#closeButton').click(function() {
        $('#enter_event_modal').modal('hide');
      });
 
      $('#date_wrapper').datepicker().on('changeDate', function(){
          $(this).datepicker('hide');
      });
      
      $("form").submit(function() {
        $.post("create", $(this).serialize(), function() {
          eventTable.fnDraw();
          $('#enter_event_modal').modal('hide');
        } );
        return false;
      });
    }

    this.eventTable = function() {
      var eventTable = $('#eventTable').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": "/events/update_datatable",
        "sPaginationType": "bootstrap",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "event_date", "sWidth": '15%', "bSearchable": false },
          { "mData": "description", "sWidth": '55%' },
          { "mData": "location", "sWidth": '15%' },
          { "mData": "distance", "sWidth": '15%', "bSearchable": false }
        ]
      });

      return eventTable;
    }
}

var events = new Events();
