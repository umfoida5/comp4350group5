(function($){$(document).ready(function() {
      $('#athleteTable').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sPaginationType": "bootstrap",
        "sAjaxSource": "update_datatable",
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "aoColumns": [
          { "mData": "first_name" },
          { "mData": "last_name" },
          { "mData": "email" },
          { "mData": "about_me" }
          //~ { "mData": "about_me" }
        ]
      } );
    } );
})(jQuery);
