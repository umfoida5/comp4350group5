require 'date'

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

When(/^I touch the navbar item "(.*?)"$/) do |tab_button|
    check_element_exists "view:'UITabBarButton' marked:'#{tab_button}'"
    touch "view:'UINavigationItemButtonView' marked:'#{tab_button}'"
    sleep 2
end

###
#
# Enters login credentials for the iOS Page
###
When(/^I log in$/) do
    text_field_selector = "view:'UITextField' marked:'userNameLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'passwordLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    sleep 2
    touch "view:'UIRoundedRectButton' marked:'Login'"
    sleep 2
end

###
#
# Enters invalid login credentials
###
When(/^I enter an invalid log in password$/) do
    text_field_selector = "view:'UITextField' marked:'userNameLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'passwordLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "incorrect_password"
    frankly_map text_field_selector, "endEditing:", true
    sleep 2
    touch "view:'UIRoundedRectButton' marked:'Login'"
    sleep 2
end

###
#
# Enters invalid login credentials
###
When(/^I enter an invalid log in$/) do
    text_field_selector = "view:'UITextField' marked:'userNameLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "this_is_an_invalid_login"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'passwordLogin'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "some_password"
    frankly_map text_field_selector, "endEditing:", true
    sleep 2
    touch "view:'UIRoundedRectButton' marked:'Login'"
    sleep 2
end

###
#
# Signs up with an existing id
###
When(/^I signup with an existing id$/) do
    text_field_selector = "view:'UITextField' marked:'signupUsername'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'signupPassword'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'signupFirstName'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'signupLastName'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    sleep 2
    touch "view:'UIRoundedRectButton' marked:'Sign up'"
    sleep 2
end

###
#
# Signs up with a valid id
###
When(/^I signup with a new id$/) do
    
    current_time = Time.now;
    new_user = "newuser#{current_time.year}#{current_time.month}#{current_time.day}#{current_time.hour}#{current_time.min}#{current_time.sec}"
    
    text_field_selector = "view:'UITextField' marked:'signupUsername'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", new_user
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'signupPassword'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'signupFirstName'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'signupLastName'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "frank"
    frankly_map text_field_selector, "endEditing:", true
    
    sleep 2
    touch "view:'UIRoundedRectButton' marked:'Sign up'"
    sleep 2
end

###
#
# Signs up with a valid id
###
When(/^I enter a new activity$/) do
        
    text_field_selector = "view:'UITextField' marked:'newActivityDuration'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "12"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'newActivityMaxSpeed'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "12"
    frankly_map text_field_selector, "endEditing:", true
    
    text_field_selector = "view:'UITextField' marked:'newActivityDistance'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "12"
    frankly_map text_field_selector, "endEditing:", true
    
    sleep 2
    touch "view:'UINavigationButton' marked:'Add'"
    sleep 2
end

###
#
# Signs up with a valid id
###
When(/^I enter a new goal$/) do
    
    text_field_selector = "view:'UITextField' marked:'newGoalQuantity'"
    check_element_exists(text_field_selector);
    touch text_field_selector
    frankly_map text_field_selector, "setText:", "12"
    frankly_map text_field_selector, "endEditing:", true
        
    sleep 2
    touch "view:'UINavigationButton' marked:'Add'"
    sleep 2
end


###
#
# Tests to see that we are on the proper screen view
#
###
Then (/^I should be on the Home screen$/) do
    check_element_exists "view:'UINavigationItemView' marked:'Home'"
end

Then (/^I should be on the Profile screen$/) do
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
###
Then (/^I should see a valid goal$/) do
    check_element_exists "view:'UILabel' marked:'COMPLETED! Run 12 (Between: 02/26/2013 00:00:00 and 02/27/2013 00:00:00)'"
end

Then (/^I should see the new goal$/) do
    check_element_exists "view:'UILabel' marked:'COMPLETED! Run 12 (Between: #{Time.now.strftime('%m/%d/%Y')} 00:00:00 and #{Time.now.strftime('%m/%d/%Y')} 00:00:00)"
end

Then (/^I should see a valid activity$/) do
    check_element_exists "view:'UILabel' marked:'(2013-03-05) Run: 12 km in 12 mins (Max Speed: 12 km/h)'"
end

Then (/^I should see the new activity$/) do
    check_element_exists "view:'UILabel' marked:'(#{Time.now.strftime('%Y-%m-%d')}) Run: 12 km in 12 mins (Max Speed: 12 km/h)'"
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

###
#
# verrifies that the logout and login buttons are shown
###
Then (/^I should see the login button$/) do
    sleep 2
    check_element_exists "view:'UINavigationButton' marked:'Login'"
end

Then (/^I should see the logout button$/) do
    sleep 2
    check_element_exists "view:'UINavigationButton' marked:'Logout'"
end