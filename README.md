# api_test_demo
* environment -- python 3.8, Pytest, Request, Allure

# directory introduction
* api -- template api code which can be called by other module
* data -- test data management
* report -- test report file
* scripts -- test scripts' directory
* tools -- tools directory
* app.py -- code for executing all the tests
* pytest.ini -- config file of pytest

# instructions on running the tests
1. Set up python 3.8 and allure on your local machine (FYI, the steps of installing allure can be referenced in "https://www.csdn.net/tags/MtTaMg3sOTM0ODIzLWJsb2cO0O0O.html")
2. Open the root of the project on an IDE (VSCode or Pycharm)
3. Open Terminal, run "pip install -r requirements.txt" (Need to install pip first if it was not installed)
4. This project has been configured to run sample tests on a free online testing api "jsonplaceholder.typicode.com"
5. Run the file "app.y"
6. After running the tests, open Terminal, run "allure serve ./report" to view the test report
