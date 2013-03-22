Feature: 
  COMP 4350 GROUP 5
  Frank iOS UI Testing!
  Tests Login Logout Functionality

##################################################
# Tests login/logout functionality of the app
##################################################
Scenario: 
    Tests Login/Logout Functionality with an invalid user
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
Then I should see the login button

When I touch the button marked "Login"

When I log in
Then I should be on the Home screen
Then I should see the logout button

When I touch the button marked "Logout"
Then I should see the login button

Scenario:
    Tests Login/Logout Functionality with a valid login, an invalid user and an invalid password
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
Then I should see the login button

When I touch the button marked "Login"
When I enter an invalid log in
Then I should see "Invalid username."

Scenario: 
    Tests Login/Logout Functionality with an invalid password
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
Then I should see the login button

When I touch the button marked "Login"
When I enter an invalid log in password
Then I should see "Incorrect password."
