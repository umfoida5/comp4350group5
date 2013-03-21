def app_path
  ENV['APP_BUNDLE_PATH'] || (defined?(APP_BUNDLE_PATH) && APP_BUNDLE_PATH)
end

Given /^I launch the app$/ do
  # latest sdk and iphone by default
  launch_app app_path, ipad
end

Given /^I launch the app using iOS (\d\.\d)$/ do |sdk|
  # You can grab a list of the installed SDK with sim_launcher
  # > run sim_launcher from the command line
  # > open a browser to http://localhost:8881/showsdks
  # > use one of the sdk you see in parenthesis (e.g. 4.2)
  launch_app app_path, sdk
end

###
#
# Launches IPAD application with ios 6.1
###
Given /^I launch the app using iOS (\d\.\d) and the (iphone|ipad) simulator$/ do |sdk, version|
  launch_app app_path, sdk, version
end

<<<<<<< Updated upstream
###
#
# Changes views using the navigation bar buttons
###
When(/^I navigate to "(.*?)"$/) do |tab_button|
    check_element_exists "view:'UITabBar'"
    check_element_exists "view:'UITabBarButton' marked:'#{tab_button}'"
    touch "view:'UITabBar' view:'UITabBarButton' marked:'#{tab_button}'"
    sleep 2
end


When(/^I enter login credentials$/) do
    text_field_selector = "view:'UITextField' marked:'userNameLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "justin"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'passwordLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "justin"
    frankly_map text_field_selector, "endEditing:", true
end

###
#
# Tests to see that we are on the proper screen view
#
###
Then (/^I should be on the Home screen$/) do
    check_element_exists "view:'UITextField' marked:'passwordLogin'"
=======
When(/^I navigate to "(.*?)"$/) do |tab_button|
    touch "view:'UITabBarButton' marked:'#{tab_button}'"
end

# Screen view checks
Then (/^I should be on the Home screen$/) do
>>>>>>> Stashed changes
    check_element_exists "view:'UINavigationItemView' marked:'Home'"
end

Then (/^I should be on the Profile screen$/) do
<<<<<<< Updated upstream
    check_element_exists "view:'UINavigationItemView' marked:'Profile'"
end

Then (/^I should be on the Activities screen$/) do
    check_element_exists "view:'UINavigationItemView' marked:'Activities'"
end

Then (/^I should be on the Goals screen$/) do
    check_element_exists "view:'UINavigationItemView' marked:'Goals'"
end

Then (/^I should be on the Events screen$/) do
    check_element_exists "view:'UINavigationItemView' marked:'Events'"
end

Then (/^I should be on the About screen$/) do
    check_element_exists "view:'UINavigationItemView' marked:'About'"
end

###
#
#
#
###
Then (/^I should see a valid goal$/) do
    check_element_exists "view:'UILabel' marked:'COMPLETED! Walk 100 (Between: 04/11/2013 21:54:55 and 05/06/2013 21:54:55)'"
end

Then (/^I should see a valid activity$/) do
    check_element_exists "view:'UILabel' marked:'(2013-03-05) Bike: 35 km in 60 mins (Max Speed: 55 km/h)'"
end

Then (/^I should see a valid event$/) do
    check_element_exists "view:'UILabel' marked:'(2013-03-17) Do not miss La Tour De France! Find... (paris) (10km)'"
end

Then (/^I should see a valid profile$/) do
    check_element_exists "view:'UILabel' marked:'Justin Fdart'"
end

Then (/^I should see a valid about$/) do
    check_element_exists "view:'UILabel' marked:'CardioQuest'"
end
=======
    check_element_exists "view:'UILabel' marked:'Badges'"
end

Then (/^I should be on the Activities screen$/) do
    check_element_exists "view:'UINavigationBar' view:'UINavigationItemView' marked:'Activities'"
end

# Login Functionality
# Then
>>>>>>> Stashed changes
