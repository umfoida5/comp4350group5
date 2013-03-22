Feature: 
  COMP 4350 GROUP 5
  Frank iOS UI Testing!
  Tests Navigation Bar Button

##################################################
# Tests Navigation Bar Buttons on iPad
##################################################
Scenario:
    Navigation through the nav bar button items
Given I launch the app using iOS 6.1 and the ipad simulator

When I navigate to "Home"
Then I should be on the Home screen

When I navigate to "Activities"
Then I should be on the Activities screen

When I navigate to "Profile"
Then I should be on the Profile screen

When I navigate to "Goals"
Then I should be on the Goals screen

When I navigate to "Events"
Then I should be on the Events screen

When I navigate to "About"
Then I should be on the About screen
