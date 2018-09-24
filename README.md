# General information

This project contains simple UI test written in Python+Selenium and [Allure Report](https://cdn.rawgit.com/alderven/pizzade/master/allure-report/index.html)

# Test Case and Test Result:
№ | Test Script                                                                                    | Test description                                 | Run Result                                                                                                       
-- | -----------------------------------------------------------------------------------------------| -------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------- 
1  | [test_pizzade_login.py](https://github.com/alderven/pizzade/blob/master/test_pizzade_login.py) | Log in with correct credentials                  | [Passed](https://cdn.rawgit.com/alderven/pizzade/master/allure-report/index.html#behaviors/cc1460ab704b97cd9991bc6dd4123a2c/fdde9a10c123267e/)
2  | [test_pizzade_login.py](https://github.com/alderven/pizzade/blob/master/test_pizzade_login.py) | Log in with correct email and incorrect password | [Passed](https://cdn.rawgit.com/alderven/pizzade/master/allure-report/index.html#behaviors/cc1460ab704b97cd9991bc6dd4123a2c/19a0f0b1d37120fc/)
3  | [test_pizzade_login.py](https://github.com/alderven/pizzade/blob/master/test_pizzade_login.py) | Log in with incorrect email and correct password | [Passed](https://cdn.rawgit.com/alderven/pizzade/master/allure-report/index.html#behaviors/cc1460ab704b97cd9991bc6dd4123a2c/c7eec5b7945990bd/)
4  | [test_pizzade_login.py](https://github.com/alderven/pizzade/blob/master/test_pizzade_login.py) | Log in with incorrect email and password         | [Passed](https://cdn.rawgit.com/alderven/pizzade/master/allure-report/index.html#behaviors/cc1460ab704b97cd9991bc6dd4123a2c/fcb9a04282b88048/)  


# How to install
1. Download and unzip this project: https://github.com/alderven/pizzade/archive/master.zip
1. Install Python 3.6 or higher: https://www.python.org/downloads/
1. Install following Python libs:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * selenium: https://pypi.python.org/pypi/selenium
   * allure-pytest: https://pypi.python.org/pypi/allure-pytest
   * configparser: https://pypi.python.org/pypi/configparser
1. Download ChromeDriver driver to the project root folder:
   http://chromedriver.chromium.org/downloads
1. Install Allure Framework. See detailed instruction: https://docs.qameta.io/allure/latest/


# How to run tests
Execute following line in CMD in the project folder:
```
python -m pytest --alluredir /full/path/to/report/folder
```

# How to generate Allure report
Execute following line in CMD in the project folder:
```
allure serve /full/path/to/report/folder
```