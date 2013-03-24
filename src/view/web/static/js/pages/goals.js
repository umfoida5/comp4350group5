

  function EnterButton($){$('#enterButton').click(function() {
    $('#enter_goal_modal').modal('show');
    $('#activity').attr('value', '');
    $('#operator').attr('value', 'total');
    $('#quantity').attr('value', '');
    $('#metric').attr('value', 'distance');
    $('#start_date').attr('value', '');
    $('#end_date').attr('value', '');
  });}

  function CloseButton($){
    $('#closeButton').click(function() {
      $('#enter_goal_modal').modal('hide');
    });
  }
  function GoalsTable($){
    return $('#goalsTable').dataTable( {
    "bProcessing": true,
    "bServerSide": true,
    //"bLengthChange": false,
    "sPaginationType": "bootstrap",
    "sAjaxSource": "update_datatable",


    "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
    

    "aoColumns": [
      { "mData": "activity", "bSearchable": false },
      { "mData": "operator", "bSearchable": false },
      { "mData": "quantity", "bSearchable": false },
      { "mData": "metric", "bSearchable": false },
      { "mData": "start_date", "bSearchable": false },
      { "mData": "end_date", "bSearchable": false },
      { "mData": "completed", "bSearchable": false,
        "mRender": function( data, type, row) {
            if (data == true) {
                return 'Yes ';
            } else {
                return 'No ';
            }
        }
      }
    ]
  } );}

  // for submitting the new goal
  function Form($, goalsTable){$("form").submit(function() {
    $.post("create", $(this).serialize(), function() {
      goalsTable.fnDraw();
      $('#enter_goal_modal').modal('hide');
    } );
    return false;
  });}

  // for the start and end date inputs
  function StartDate($){$('#start_date').datepicker().on('changeDate', function(){
      $(this).datepicker('hide');
  });}
  
function EndDate($){$('#end_date').datepicker().on('changeDate', function(){
      $(this).datepicker('hide');
  });}

  
