
var target = UIATarget.localTarget();

target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textFields()["userNameLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().secureTextFields()["passwordLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().buttons()["Login"].tap();
target.frontMostApp().tabBar().buttons()["Activities"].tap();
target.frontMostApp().navigationBar().leftButton().tap();
target.frontMostApp().mainWindow().buttons()["Tuesday, February 26, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Wednesday, February 20, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Wednesday, February 27, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Friday, March 1, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Thursday, March 14, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Friday, March 22, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Wednesday, March 20, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Monday, March 18, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Friday, March 8, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Sunday, March 10, 2013"].tap();
target.frontMostApp().mainWindow().buttons()["Sunday, March 24, 2013"].tap();
target.frontMostApp().navigationBar().leftButton().tap();
target.frontMostApp().navigationBar().rightButton().tap();
target.waitForInvalid();

target.frontMostApp().mainWindow().pickers()[1].wheels()[2].tapWithOptions({tapOffset:{x:0.45, y:0.42}});
target.frontMostApp().mainWindow().pickers()[1].wheels()[3].tapWithOptions({tapOffset:{x:0.29, y:0.40}, duration:1.0});
target.frontMostApp().mainWindow().textFields()["newActivityDuration"].tap();
target.frontMostApp().keyboard().typeString("20");
target.frontMostApp().mainWindow().textFields()["newActivityDistance"].tap();
target.frontMostApp().keyboard().typeString("20");
target.frontMostApp().mainWindow().textFields()["newActivityMaxSpeed"].tap();
target.frontMostApp().keyboard().typeString("20");
target.tap({x:622.00, y:698.00});
target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().navigationBar().leftButton().tap();
target.waitForInvalid();

target.frontMostApp().tabBar().buttons()["Home"].tap();
target.frontMostApp().navigationBar().leftButton().touchAndHold(1.1);
target.frontMostApp().tabBar().buttons()["Activities"].tap();
target.waitForInvalid();
target.frontMostApp().tabBar().buttons()["Home"].tap();

UIALogger.logPass("TestActivities");