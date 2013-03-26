
var target = UIATarget.localTarget();

target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textFields()["userNameLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().secureTextFields()["passwordLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().buttons()["Login"].tap();
target.frontMostApp().tabBar().buttons()["Goals"].tap();
target.frontMostApp().mainWindow().tableViews()["Empty list"].cells()["ONGOING! Swim 100 (Between: 2013-04-20 and 2013-05-15)"].staticTexts()["ONGOING! Swim 100 (Between: 2013-04-20 and 2013-05-15)"].scrollToVisible();
target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().pickers()[0].wheels()[1].tapWithOptions({tapOffset:{x:0.48, y:0.48}});
target.frontMostApp().mainWindow().pickers()[0].wheels()[2].tapWithOptions({tapOffset:{x:0.49, y:0.65}});
target.frontMostApp().mainWindow().textFields()["newGoalQuantity"].tap();
target.frontMostApp().keyboard().typeString("20");
target.tap({x:591.00, y:700.00});
target.frontMostApp().navigationBar().rightButton().tap();
target.waitForInvalid();
target.frontMostApp().tabBar().buttons()["Home"].tap();
target.waitForInvalid();

target.frontMostApp().navigationBar().leftButton().tap();

target.frontMostApp().tabBar().buttons()["Goals"].tap();
target.frontMostApp().tabBar().buttons()["Home"].tap();

UIALogger.logPass("TestGoals");