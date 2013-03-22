Feature: 
  COMP 4350 GROUP 5
  Frank iOS UI Testing!
  Test goals functionality

##################################################
# Tests signup functionality with an existing id
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

When I navigate to "Events"
Then I should be on the Events screen
Then I should see a valid event

When I touch the button marked "Post an Event"
When I enter a new event
Then I should be on the Events screen
#Then I should see the new goal