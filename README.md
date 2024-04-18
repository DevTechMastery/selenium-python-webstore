# Test automation framework for [Demo Web Store](http://happyharbor.com) application
![logo.png](src/readme_page_media/logo/Logo.png)

## Overview

The myStoreWebUI project is a [Python-based](https://www.python.org/) web automation framework designed to interact with an online store's user interface.   
It uses Selenium WebDriver for browser automation and pytest for test organization and execution.  

The project is structured around a Page Object Model (POM) design pattern, which helps to maintain the code and reduce code duplication.                    
Each page of the web application is represented by a Python class, and the interactions with the page are encapsulated as methods on these classes.

The project is designed to be flexible and maintainable, with the ability to add new tests and page classes as the web application evolves.

In addition to UI tests, the framework also includes API tests. These tests interact directly with the web application's backend, verifying the correct operation of the API endpoints. This allows for more comprehensive coverage of the application's functionality, as well as faster and more reliable tests compared to UI tests.

Continuous integration is an essential part of the project, with Jenkins used to automate the test execution process. Jenkins is configured to run the tests on a regular schedule, providing feedback on the application's health and stability.

Notifications are sent to the team via Slack, and test results are visualized using Allure reports and Allure TestOps.


## Technology Stack

| <a href="https://www.python.org/"><img src="src/readme_page_media/logo/Python.png" width="40" height="40"  alt="Python"/></a> | <a href="https://www.jetbrains.com/pycharm/"><img src="src/readme_page_media/logo/PyCharm.png" width="40" height="40"  alt="PyCharm"/></a> | <a href="https://github.com/"><img src="src/readme_page_media/logo/GitHub.png" width="40" height="40"  alt="GitHub"/></a> | <a href="https://docs.pytest.org/en/8.0.x/contents.html"><img src="src/readme_page_media/logo/Pytest.png" width="40" height="40"  alt="Pytest"/></a> | <a href="https://www.selenium.dev/"><img src="src/readme_page_media/logo/Selenium.png" width="40" height="40"  alt="selenium"/></a>  | <a href="https://www.jenkins.io/"><img src="src/readme_page_media/logo/Jenkins.png" width="40" height="40"  alt="jenkins"/></a> |
|:-----------------------------------------------------------------------------------------------------------------------------:| :---------: | :---------: | :---------: | :---------: | :---------: |
|                                                            Python                                                             | PyCharm | GitHub | Pytest | Selenium | Jenkins |

| <a href="https://www.atlassian.com/software/jira"><img src="src/readme_page_media/logo/Jira.png" width="40" height="40"  alt="Jira"/></a> | <a href="https://allurereport.org/"><img src="src/readme_page_media/logo/Allure.png" width="40" height="40"  alt="Allure"/></a> |<a href="https://docs.qameta.io/allure-testops//"><img src="src/readme_page_media/logo/AllureTO.png" width="40" height="40"  alt="AllureTestOps"/></a> | <a href="https://slack.com/"><img src="src/readme_page_media/logo/Slack.png" width="40" height="40"  alt="Slack"/></a> | <a href="https://www.jetbrains.com/idea/"><img src="TBD" width="40" height="40"  alt="TBD"/></a> |<a href="https://www.jetbrains.com/idea/"><img src="TBD" width="40" height="40"  alt="TBD"/></a> |
| :---------: | :---------: | :---------: | :---------: | :---------: | :---------: |
| Jira | Allure | Allure TO | Slack | TBD | TBD |


The `myStoreWebUI` test automation framework is built using a modern technology stack that includes Python, Selenium WebDriver, pytest, and Jenkins among others. This combination of technologies allows for robust, scalable, and maintainable automated testing of the web application's user interface.




There are several tools are used:

* [Selenium](https://www.selenium.dev/) is a tool for automating across different browsers and platforms.
* [Jenkins](https://www.jenkins.io/) is a continuous integration system to launch the tests
* [Jira](https://www.atlassian.com/software/jira) is an issue tracking system
* [Allure Report](http://allure.qatools.ru) and [Allure TestOps](https://docs.qameta.io/allure-testops/) are used to visualize test results
* [Slack](https://slack.com/) is a custom chanel using to notify about the test result
* [TBD](https://slack.com/) TBD...............................

## UI Tests

:heavy_check_mark: UI Register a new user

:heavy_check_mark: UI Login test with incorrect credentials

:heavy_check_mark: Validate authorized users can add a product to cart

:heavy_check_mark: TBD    

## API Tests
:heavy_check_mark: Add product to cart with API

:heavy_check_mark: TBD   


## Launch the tests

### To run the tests locally (default):

```
pytest -m tcid
```

### Video sample with passing test case:
![Selenium](./images/register.gif)

### Jenkins job: Possible launch configurations
![Jenkins](./images/jenkins.png)

### Allure report: Test status and trend graphs
![Allure1](./images/alllure_grapths.png)
![Allure2](./images/allure_report.png)

### Allure Test Ops: Test result of the launch
#### There is an example of the failed automated test with attachments.
![TestOps](./images/failed_test.png)

### Allure Test Ops: Test analytics dashboard
![Dashboard1](./images/Overview.png)

### Allure Test Ops: Analytics by success rate and duration rate 
![Dashboard2](./images/Automatio-types.png)

### Integration with Jira: Test results and Test launch are attached to the Jira ticket
![Jira](./images/jira-ticket.png)

### Slack notification
![Slack](./images/slack.png)

