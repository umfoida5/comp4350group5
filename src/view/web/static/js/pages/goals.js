function Goals() {
 
  this.controls = function() {
      $('#enterButton').click(function() {
        $('#enter_goal_modal').modal('show');
        $('#activity').attr('value', 'Run');
        $('#operator').attr('value', 'Total');
        $('#quantity').attr('value', '');
        $('#metric').attr('value', 'distance');
        $('#start_date').datepicker('setValue', new Date());
        $('#start_date').datepicker('update');
        $('#end_date').datepicker('setValue', new Date((new Date()).getTime() + 24 * 60 * 60 * 1000));
        $('#end_date').datepicker('update');
      });

      $('#closeButton').click(function() {
        $('#enter_goal_modal').modal('hide');
      });

      
      // for the start and end date inputs
      $('#start_date').datepicker().on('changeDate', function(){
          $(this).datepicker('hide');
      });
      
      $('#end_date').datepicker().on('changeDate', function(){
          $(this).datepicker('hide');
      });

      $('#start_date input').click(function() {
          this.blur();
          $('#start_date').datepicker('show');
      });

      $('#end_date input').click(function() {
          this.blur();
          $('#end_date').datepicker('show');
      });
  }

  this.goalsTable = function() {
      var goalsTable = $('#goalsTable').dataTable({
        "bProcessing": true,
        "bServerSide": true,
        "bFilter"    : false,
        "sPaginationType": "bootstrap",
        "sAjaxSource": "/goals/update_datatable",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "activity", "bSearchable": false },
          { "mData": "operator", "bSearchable": false },
          { "mData": "quantity", "bSearchable": false },
          { "mData": "metric", "bSearchable": false },
          { "mData": "start_date", "bSearchable": false, 'sClass':'hidden-phone' },
          { "mData": "end_date", "bSearchable": false, 'sClass':'hidden-phone' },
          { "mData": "completed", "bSearchable": false, 'sClass':'hidden-phone',
            "mRender": function( data, type, row) {
                if (data == true) {
                    return 'Yes ';
                } else {
                    return 'No ';
                }
            }
          }
        ]
      });
      
      // for submitting the new goal
      $("form").submit(function() {
        $.post("create", $(this).serialize(), function() {
          goalsTable.fnDraw();
          $('#enter_goal_modal').modal('hide');
        } );
        return false;
      });

      
      return goalsTable;
  }
}

var goals = new Goals();
