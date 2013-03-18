Feature: 
  COMP 4350 GROUP 5
  Frank iOS UI Testing!

##################################################
# Tests the login/home page of the application
##################################################
Scenario: 
    Navigation through the nav bar button items
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
When I enter login credentials
When I touch the button marked "Login"

##################################################
# Tests Navigation Bar Buttons on iPad
##################################################
Scenario: 
    Navigation through the nav bar button items
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
When I enter login credentials
#When I touch the button marked "Login"

When I navigate to "Activities"
Then I should be on the Activities screen

When I navigate to "Profile"
Then I should be on the Profile screen

When I navigate to "Home"
Then I should be on the Home screen

When I navigate to "Goals"
Then I should be on the Goals screen

When I navigate to "Events"
Then I should be on the Events screen

When I navigate to "About"
Then I should be on the About screen


##################################################
# Tests Navigation Bar Buttons on iPad
##################################################
Scenario: 
    Navigation through the nav bar button items
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
When I enter login credentials
When I touch the button marked "Login"

When I navigate to "Profile"
Then I should be on the Profile screen

When I navigate to "Activities"
Then I should be on the Activities screen
Then I should see a valid activity

When I navigate to "Goals"
Then I should be on the Goals screen
Then I should see a valid goal

When I navigate to "Events"
Then I should be on the Events screen
Then I should see a valid event

When I navigate to "About"
Then I should be on the About screen


##################################################
# Tests Rotation Features of the iPad
##################################################
Scenario: 
    Tests the rotation capabilities of the iPad
Given I launch the app using iOS 6.1 and the ipad simulator
Given the device is in landscape orientation
Given the device is in portrait orientation
Given the device is in landscape orientation
Given the device is in portrait orientation
