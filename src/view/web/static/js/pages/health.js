function Health() {
  var healthTable;
  this.controls = function() {
      $('#enterButton').click(function() {
        var date = new Date();
        $('#enter_health_modal').modal('show');
        $('#date_wrapper_form').datepicker('setValue', (date.getDate()) + "-" + (date.getMonth() + 1) + "-" + (date.getFullYear()));
        $('#weight').attr('value', '');
        $('#resting_heart_rate').attr('value', '');
        $('#comment').attr('value', '');
      });
      
      $('#closeButton').click(function() {
        $('#enter_health_modal').modal('hide');
      });

      $('#graph_from_date_div').datepicker();
      $('#graph_to_date_div').datepicker();
      $('#date_wrapper_form').datepicker();
      
      $('form').submit(function() { 
        $.post("create", $(this).serialize(), function() {
            $('#enter_health_modal').modal('hide');
            update_graph();       
            healthTable.fnDraw();
        });
        return false;
      });

    // Makes asynchronous call to update graph based on date range.
    var update_graph = function () {
      $.ajax( {
          "dataType": 'json',
          "type": "GET",
          "url": "/health/json",
          "data": {start_date : $('#graph_from_date').attr('value') , end_date : $('#graph_to_date').attr('value')},
          "success": drawGraph
      })
    }

    update_graph();

    $('#updateGraphBtn').click(function() {
      update_graph();
    });

    // Callback function to update graph
    function drawGraph(json) {
    var graphData = new Array();

    $.each(json.health, function() {
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

    if (graphData.length <= 0) {
        chart.showLoading("No Health Data Recorded");
    } else {
        chart.hideLoading();
    }

    }
  }
  
  this.healthTable = function() {
      healthTable = $('#healthTable').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": "/health/update_datatable",
        "bFilter"    : false,
        "sPaginationType": "bootstrap",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "health_date", "sWidth": '15%', "bSearchable": false },
          { "mData": "weight", "sWidth": '15%',"bSearchable": false },
          { "mData": "resting_heart_rate", "sWidth": '15%', "bSearchable": false, 'sClass':'hidden-phone' },
          { "mData": "comments", "sWidth": '55%', "bSearchable": false, 'sClass':'hidden-phone' }
        ],
        "fnServerData": function ( sSource, aoData, fnCallback, oSettings ) {
            oSettings.jqXHR = $.ajax( {
            "dataType": 'json',
            "type": "GET",
            "url": sSource,
            "data": aoData,
            "success": fnCallback
            });
        }
      });

      return healthTable;
  }
}

var health = new Health();
