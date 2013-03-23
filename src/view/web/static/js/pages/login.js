 function login($){$("#loginForm").submit(function() {
		formData = $(this).serialize();
        $.post("do_login", formData, function(errorMsg) {
          if (errorMsg == "Login was successful.") {
            window.location.href = "../profiles";
          }
          else {
            $("#loginMessage").text(errorMsg);
          }
        } );
        return false;
      } );
}

function signup($){
      $("#signupForm").submit(function() {
        $.post("signup", $(this).serialize(), function(errorMsg) {
		  if(errorMsg == "Login was successful.") {
		    window.location.href = "../profiles";
                  } else {
		    $("#signupMessage").text(errorMsg);
                  }
		} );
        return false;
      } );
}