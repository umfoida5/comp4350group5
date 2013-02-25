function Activities(url){
    
    this.enter_btn = function(){
        $('#enterButton').click(function() {
            $('#enter_activity_modal').modal('show');
            $('#type').attr('value', '');
            $('#distance').attr('value', '');
            $('#duration').attr('value', '');
            $('#max_speed').attr('value', '');
            $('#date').attr('value', '');
        });
    }
    
    this.close_btn = function(){
        $('#closeButton').click(function() {
        $('#enter_activity_modal').modal('hide');
      });
    }
    
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
        ]
      } );
      
      return athleteTable;
    }

    this.formSubmit = function(athleteTable){
        $("form").submit(function() {
        $.post("create", $(this).serialize(), function() {
          athleteTable.fnDraw();
          $('#enter_activity_modal').modal('hide');
        } );
        return false;
      } );
    }
    
    this.datepicker = function(){ $('#dateInput').datepicker(); }
}

var activity = new Activities("http://localhost:8080/");
