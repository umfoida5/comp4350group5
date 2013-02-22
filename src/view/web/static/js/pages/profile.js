(function($){
    $(document).ready(function(){
      var athlete;
      $.getJSON('athlete', athlete, function(athlete){
        $("#profile_name").append(athlete['first_name'] + " " + athlete['last_name']);
        $("#dob").html(athlete['birth_date']);
        $("#address").html(athlete['address']);
        $("#email").html(athlete['email']);
        $("#about_me").html(athlete['about_me']);
      }); 
      
      $.getJSON('get_unlocked_achievements', function(unlocked_achievements){
        $.each(unlocked_achievements, function(index) {
          var achievement = unlocked_achievements[index].achievement;
          var unlocked_date = unlocked_achievements[index].unlocked_date;
          $("#" + achievement.title + " img#image").attr("src", achievement.image_url);
          $("#" + achievement.title + " p#date").text(unlocked_date);
          $("#" + achievement.title + " a").attr("href", "#");
        });
      });

      $('#dob').editable('update_dob', {
          indicator: 'Saving',
          tooltip:  'Click to change',
          onblur: 'cancel',
          submit: 'OK',
          cancel: 'Cancel',
          name: 'birth_date',
          //~ method: 'PUT',
          type: 'text',
          intercept: function (jsondata) {
            obj = jQuery.parseJSON(jsondata);
            // do something with obj.status and obj.other
            return(obj.birth_date);
          }        
        });
        
      $('#address').editable('update_address', {
          indicator: 'Saving',
          tooltip:  'Click to change',
          onblur: 'cancel',
          submit: 'OK',
          cancel: 'Cancel',
          name: 'address',
          //~ method: 'PUT',
          type: 'text',
          intercept: function (jsondata) {
            obj = jQuery.parseJSON(jsondata);
            // do something with obj.status and obj.other
            return(obj.address);
          }
        });
        
        
      $('#email').editable('update_email', {
          indicator: 'Saving',
          tooltip:  'Click to change',
          onblur: 'cancel',
          submit: 'OK',
          cancel: 'Cancel',
          name: 'email',
          //~ method: 'PUT',
          type: 'text',
          intercept: function (jsondata) {
            obj = jQuery.parseJSON(jsondata);
            // do something with obj.status and obj.other
            return(obj.email);
          }
        
        });
        
        
        $('#about_me').editable('update_about', {
          indicator: 'Saving',
          tooltip:  'Click to change',
          onblur: 'cancel',
          submit: 'OK',
          cancel: 'Cancel',
          name: 'about_msg',
          //~ method: 'PUT',
          type: 'text',
          intercept: function (jsondata) {
            obj = jQuery.parseJSON(jsondata);
            // do something with obj.status and obj.other
            return(obj.about_me);
          }
        });
    });
}) (jQuery);
