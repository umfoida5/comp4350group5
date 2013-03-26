
var target = UIATarget.localTarget();

target.frontMostApp().navigationBar().rightButton().tap();
target.frontMostApp().mainWindow().textFields()["signupUsername"].tap();
target.frontMostApp().keyboard().typeString("testsignu");
target.frontMostApp().keyboard().keys()["Delete"].tap();
target.frontMostApp().keyboard().typeString("up");
target.frontMostApp().mainWindow().secureTextFields()["signupPassword"].tap();
target.frontMostApp().keyboard().typeString("testsignup");
target.frontMostApp().mainWindow().textFields()["signupLastName"].tap();
target.frontMostApp().mainWindow().secureTextFields()["signupPassword"].tap();
target.frontMostApp().keyboard().keys()["Delete"].tapWithOptions({tapCount:3});
target.frontMostApp().keyboard().typeString("qw");
target.frontMostApp().mainWindow().buttons()["Sign up"].tap();
target.tap({x:600.00, y:651.00});
target.frontMostApp().navigationBar().leftButton().tap();

UIALogger.logPass("TestLogin");