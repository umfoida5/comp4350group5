function Profile(){
  
     this.isEmail = function (value){

        var valid = true;

        if (value != null) { 
          var str = value.toString();
          var atpos = str.indexOf("@");
          var dotpos = str.lastIndexOf(".");
          if(atpos < 1 || dotpos <atpos+2 || dotpos+2>=str.length){
            valid = false;
          }
        }else{
          valid = false;
        }
        return valid;
      }
      
      this.isDate = function(value){
        var valid = false;
        try{
          if(value != null && value.length > 7){
            var str = value.toString();
            var dt = new Date(str);
            valid = !(dt == "Invalid Date");
          }
        }catch(err){
          valid = false;
        }
        
        return valid;
      }
  

       this.get_athleteAjax = function(){
          
        
        var athlete = $.ajax({
            url: '../profiles/athlete',
            data: athlete,
            success: function(athlete){
           
              $("#profile_name").append(athlete['first_name'] + " " + athlete['last_name']);
              setValueIfEmptyString("#dob", athlete['birth_date'], "Click to add your birth date");
              setValueIfEmptyString("#address", athlete['address'], "Click to add your address");
              setValueIfEmptyString("#email", athlete['email'], "Click to add your email");
              setValueIfEmptyString("#about_me", athlete['about_me'], "Click to add your biography");
            }
        });
        
        return athlete; 
      }

      this.get_achievesAjax = function(){
        $.getJSON('get_unlocked_achievements', function(unlocked_achievements){
          $.each(unlocked_achievements, function(index) {
            var achievement = unlocked_achievements[index].achievement;
            var unlocked_date = unlocked_achievements[index].unlocked_date;
            $("#" + achievement.title + " img#image").attr("src", achievement.image_url);
            $("#" + achievement.title + " p#date").text(unlocked_date);
            $("#" + achievement.title + " a").attr("href", "#");
          });
        });
      }
      
      this.jeditableControl = function(){

      $('#dob').editable('update_dob', {
          onsubmit: function(settings, td){
            var profile = new Profile("");
            var input = $(td).find('input');
            var original = input.val();
            if (profile.isDate(original)) {
              console.log("Validation correct");
              return true;
            } else {
              console.log("Validation failed. Ignoring");
              input.css('background-color','#c00').css('color','#fff');
            return false;
            }
          },
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
          onsubmit: function(settings, td){
            
            var input = $(td).find('input');
            var original = input.val();
            var profile = new Profile("");
            
            if (profile.isEmail(original)) {
              console.log("Validation correct");
              return true;
            } else {
              console.log("Validation failed. Ignoring");
              input.css('background-color','#c00').css('color','#fff');
            return false;
            }
          },
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
  }
}

function setValueIfEmptyString(field, json_data, default_value)
{
  if( json_data == null || json_data == "")
  {
    $(field).html(default_value); 
  }
  else
  {
    $(field).html(json_data);
  }
}

var prof = new Profile();
