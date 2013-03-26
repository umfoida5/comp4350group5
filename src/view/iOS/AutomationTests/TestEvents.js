
var target = UIATarget.localTarget();

target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textFields()["userNameLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().secureTextFields()["passwordLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().buttons()["Login"].tap();
target.frontMostApp().tabBar().buttons()["Events"].tap();
target.frontMostApp().mainWindow().tableViews()["Empty list"].cells()["(2013-03-26) Come join us for the MSWalk. It is ... (parkland) (15km)"].staticTexts()["(2013-03-26) Come join us for the MSWalk. It is ... (parkland) (15km)"].scrollToVisible();
target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textViews()["newEventDescription"].tapWithOptions({tapOffset:{x:0.43, y:2.04}});
target.frontMostApp().keyboard().typeString("Description");
target.frontMostApp().mainWindow().textFields()["newEventCity"].tap();
target.frontMostApp().keyboard().typeString("winnipeg");
target.frontMostApp().mainWindow().textFields()["newEventDistance"].tap();
target.frontMostApp().keyboard().typeString("15");
target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().tabBar().buttons()["Home"].tap();
target.frontMostApp().navigationBar().leftButton().tap();

UIALogger.logPass("TestEvents");