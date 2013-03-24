function Health() {
  this.controls = function() {
      $('#enterButton').click(function() {
        $('#enter_health_modal').modal('show');
      });
      
      $('#closeButton').click(function() {
        $('#enter_health_modal').modal('hide');
      });

      $('#date_wrapper_start').datepicker();
      $('#date_wrapper_end').datepicker();
      $('#date_wrapper_form').datepicker();
      
      $('form').submit(function() { 
        $.post("create", $(this).serialize(), function() {
            $('#enter_health_modal').modal('hide');
            healthTable.fnDraw();
        });
        return false;
      });
  }
  
  this.healthTable = function() {
      var healthTable = $('#healthTable').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": "/health/update_datatable",
        "bFilter"    : false,
        "sPaginationType": "bootstrap",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "health_date", "sWidth": '15%', "bSearchable": false },
          { "mData": "weight", "sWidth": '15%',"bSearchable": false },
          { "mData": "resting_heart_rate", "sWidth": '15%', "bSearchable": false },
          { "mData": "comments", "sWidth": '55%', "bSearchable": false }
        ],
        "fnServerData": function ( sSource, aoData, fnCallback, oSettings ) {
            oSettings.jqXHR = $.ajax( {
            "dataType": 'json',
            "type": "GET",
            "url": sSource,
            "data": aoData,
            "success": [fnCallback, drawGraph]
            } );
        }
      });
      
      function drawGraph(json) {
        var graphData = new Array();
        
        $.each(json.aaData, function() {
            var d = new Date(this.health_date);
            graphData.push([Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()), this.weight]);
        });

        chart = new Highcharts.Chart({
            chart: {
                renderTo: 'graphContainer',
                type: 'spline'
            },            
            title: {
                text: 'Weight:'
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'Weight (lbs)'
                },
                min: 0
            },
            tooltip: {
                formatter: function() {
                        return '<b>'+ this.series.name +'</b><br/>'+
                        Highcharts.dateFormat('%e. %b', this.x) +': '+ this.y +' m';
                }
            },
            
            series: [{
                name: 'Weight',
                data: graphData
            }]
        });

      }

      return healthTable;
  }
}

var health = new Health();