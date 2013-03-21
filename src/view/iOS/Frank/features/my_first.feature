Feature: 
  As an iOS developer
  I want to have a sample feature file
  So I can see what my next step is in the wonderful world of Frank/Cucumber testing

Scenario: 
    Rotating the simulator for demonstration purposes
Given I launch the app using iOS 6.1 and the ipad simulator
Given the device is in landscape orientation
Given the device is in portrait orientation
Given the device is in landscape orientation
Given the device is in portrait orientation

When I navigate to "Home"
Then I should be on the Home screen

When I navigate to "Profile"
Then I should be on the Profile screen

When I navigate to "Activities"
Then I should be on the Activities screen

When I navigate to "Goals"
When I navigate to "Events"
When I navigate to "About"