
var target = UIATarget.localTarget();

target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textFields()["userNameLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().secureTextFields()["passwordLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().keyboard().typeString("\n");
target.frontMostApp().tabBar().buttons()["Health"].tap();
target.frontMostApp().mainWindow().pickers()[0].wheels()[0].tapWithOptions({tapOffset:{x:0.88, y:0.28}, duration:1.3});
target.frontMostApp().navigationBar().leftButton().tap();
target.waitForInvalid();
target.frontMostApp().mainWindow().textFields()["healthWeight"].tap();
target.frontMostApp().keyboard().typeString("100");
target.frontMostApp().mainWindow().textFields()["healthHeartRate"].tap();
target.frontMostApp().keyboard().typeString("50");
target.frontMostApp().mainWindow().buttons()["Save Health Record"].tap();
target.waitForInvalid();
target.frontMostApp().tabBar().buttons()["Home"].tap();
target.frontMostApp().navigationBar().leftButton().tap();
UIALogger.logPass("TestHealth");