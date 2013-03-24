function EnterButton($){
  $('#enterButton').click(function() {
        $('#enter_event_modal').modal('show');
        $('#date').attr('value', '');
        $('#location').attr('value', '');
        $('#distance').attr('value', '');
        $('#description').attr('value', '');
      });
      }

      function CloseButton($){
      $('#closeButton').click(function() {
        $('#enter_event_modal').modal('hide');
      });
      }

      function EventTable($){
        return $('#eventTable').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": "update_datatable",
        "sPaginationType": "bootstrap",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "event_date", "sWidth": '15%', "bSearchable": false },
          { "mData": "description", "sWidth": '55%' },
          { "mData": "location", "sWidth": '15%' },
          { "mData": "distance", "sWidth": '15%', "bSearchable": false }
        ]
      } );}
      
      function DateWrapper($){
      $('#date_wrapper').datepicker().on('changeDate', function(){
          $(this).datepicker('hide');
      });}

      function Form($, eventTable){
        $("form").submit(function() {
        $.post("create", $(this).serialize(), function() {
          eventTable.fnDraw();
          $('#enter_event_modal').modal('hide');
        } );

        return false;
      } );
      }
