
var target = UIATarget.localTarget();

target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textFields()["userNameLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().secureTextFields()["passwordLogin"].tap();
target.frontMostApp().keyboard().typeString("ben");
target.frontMostApp().mainWindow().buttons()["Login"].tap();
target.frontMostApp().tabBar().buttons()["Stats"].tap();
target.frontMostApp().mainWindow().pickers()[0].wheels()[0].tapWithOptions({tapOffset:{x:0.35, y:0.38}});
target.frontMostApp().mainWindow().pickers()[2].wheels()[0].tapWithOptions({tapOffset:{x:0.27, y:0.43}});
target.frontMostApp().mainWindow().pickers()[2].wheels()[0].tapWithOptions({tapOffset:{x:0.24, y:0.50}});
target.frontMostApp().tabBar().buttons()["Home"].tap();
target.frontMostApp().navigationBar().leftButton().tap();
target.frontMostApp().tabBar().buttons()["Stats"].tap();
target.frontMostApp().tabBar().buttons()["Home"].tap();
UIALogger.logPass("TestStats");