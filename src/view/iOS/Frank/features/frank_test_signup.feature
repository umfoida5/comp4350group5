Feature: 
  COMP 4350 GROUP 5
  Frank iOS UI Testing!
  Test sign up functionality

##################################################
# Tests signup functionality with an existing id
##################################################
Scenario: 
    Tests sign up functionality with a existing username
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
Then I should see the login button

When I touch the button marked "Login"
When I signup with an existing id
Then I should see "Username already exists. Please enter a new username."

##################################################
# Tests signup functionality with a valid id
##################################################
Scenario: 
    Tests sign up functionality with a existing username
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
Then I should see the login button

When I touch the button marked "Login"
When I signup with a new id
Then I should be on the Home screen
Then I should see the logout button

When I touch the button marked "Logout"
Then I should see the login button
Then I should see the login button