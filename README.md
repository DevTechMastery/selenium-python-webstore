## 📊 Test Automation Framework for the [Web Store](https://www.happyharbor.kesug.com/) Application

![logo.png](https://raw.githubusercontent.com/DevTechMastery/images/main/screenshots/demo_store_logo_pages.png)


## Technology Stack
| <a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_python.png" width="40" height="40"  alt="Python"/></a> | <a href="https://www.jetbrains.com/pycharm/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_pycharm.png" width="40" height="40"  alt="PyCharm"/></a> | <a href="https://docs.pytest.org/en/8.0.x/contents.html"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_pytest.png" width="50" height="50"  alt="Pytest"/></a> |    <a href="https://www.selenium.dev/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_selenium.png" width="40" height="40"  alt="selenium"/></a>     | <a href="https://faker.readthedocs.io/en/master/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_faker.png" width="40" height="40"  alt="Faker"/></a> | <a href="https://www.jenkins.io/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_jenkins.png" width="40" height="50"  alt="Jenkins"/></a> | <a href="https://www.docker.com/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_docker_.png" width="45" height="45"  alt="Docker"/></a> | <a href="https://github.com/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_github.png" width="45" height="45"  alt="GitHub"/></a> | <a href="https://www.atlassian.com/software/jira"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_jira.png" width="43" height="40"  alt="Jira"/></a> | <a href="https://allurereport.org/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_allure.png" width="50" height="50"  alt="Allure"/></a> | <a href="https://slack.com/"><img src="https://raw.githubusercontent.com/DevTechMastery/images/main/icons/icon_slack.png" width="40" height="40"  alt="Slack"/></a> |
|:-----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:| :---------: |:-------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                            Python                                                             |                                                                       PyCharm                                                                        |                                                                        Pytest                                                                        | Selenium |                                                            Faker                                                       |                                                             Jenkins                                                             |                                                             Docker                                                             |                                                          GitHub                                                           |                                                                   Jira                                                                    |                                                             Allure                                                              |                                                                         Slack                                                                         |

This project utilizes a variety of tools to achieve its automation goals:

* [Python](https://www.python.org/): The main programming language used for writing the test automation framework and tests.
* [PyCharm](https://www.jetbrains.com/pycharm/): An integrated development environment (IDE) used for writing and running the Python code.
* [Pytest](https://docs.pytest.org/en/latest/): A testing framework in Python, used for organizing and running the tests.
* [Selenium](https://www.selenium.dev/): A tool for automating web browsers, used for writing the UI tests.
* [Faker](https://faker.readthedocs.io/en/master/): is a Python library for generating fake data such as names, addresses, and phone numbers. It's useful for populating test data in automated tests.
* [Jenkins](https://www.jenkins.io/): A continuous integration system used to schedule and run the tests automatically.
* [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications in containers.
* [GitHub](https://github.com/): A version control system used for storing the project code and collaborating with team members.
* [Jira](https://www.atlassian.com/software/jira): An issue tracking system used for managing project tasks and bugs.
* [Allure Report](http://allure.qatools.ru): Used to visualize test results in a comprehensive and intuitive report.
* [Slack](https://slack.com/): A communication platform used for team collaboration and notifications about test results. 


## Overview
The myStoreWebUI project is a [Python-based](https://www.python.org/) web automation framework designed to interact with an online store's user interface.   
It uses Selenium WebDriver for browser automation and pytest for test organization and execution.  

The project is structured around a Page Object Model (POM) design pattern, which helps to maintain the code and reduce code duplication.                    
Each page of the web application is represented by a Python class, and the interactions with the page are encapsulated as methods on these classes.

The project is designed to be flexible and maintainable, with the ability to add new tests and page classes as the web application evolves.

Continuous integration is an essential part of the project, with Jenkins used to automate the test execution process. Jenkins is configured to run the tests on a regular schedule, providing feedback on the application's health and stability.

Notifications are sent to the team via Slack, and test results are visualized using Allure reports.

The `myStoreWebUI` test automation framework is built using a modern technology stack that includes Python, Selenium WebDriver, pytest, and Jenkins among others. This combination of technologies allows for robust, scalable, and maintainable automated testing of the web application's user interface.

## Test Scenarios
### :computer: User Interface (UI) Test Suite
***Click 👇 to Expand</ib>***    
<details>
  <summary> <b> :gear: Test Suite ★ User Authentication </b></summary>

TC ID 1 @ User Registration. \
Objective: Validate the successful registration of a new user account.

TC ID 2 @ Existing User Login. \
Objective: Authenticate an existing user and confirm successful login.

TC ID 3 @ Non-Existing User Login. \
Objective: Attempt to authenticate a non-existing user and verify that the login attempt fails with the appropriate error message.

TC ID 4 @ Existing User Login with incorrect password.  \
Objective: Authenticate an existing user with an incorrect password and verify that the login attempt fails with the appropriate error message.

TC ID 5 @ Login with empty username field.  \
Objective: Attempt to authenticate with an empty username field and verify that the login attempt fails with the appropriate error message.

TC ID 6 @ Login with empty password field. \
Objective: Attempt to authenticate with an empty password field and verify that the login attempt fails with the appropriate error message.

</details>

<details>
  <summary><b> :gear: Test Suite ★ Home Page </b></summary>

TC ID 7 @ Verify that sale badge is displayed. \
Objective: Validate the correct display of the sale badge on the home page.

TC ID 8 @ Verify that [add to cart] button is displayed for each product. \
Objective: Validate the correct display of the "Add to Cart" button for each product on the home page.

TC ID 9 @ Verify that [select option] button is displayed for variation product. \
Objective: Validate the correct display of the "Select Option" button for variation products on the home page.

TC ID 10 @ Verify that each product displays name under image. \
Objective: Validate the correct display of each product's name under the product image on the home page.

TC ID 11 @ Verify that sorting dropdown should be displayed. \
Objective: Validate the correct display of the sorting dropdown on the home page.

TC ID 12 @ Search for a Specific Product. \
Objective: Execute a product search using the search bar and confirm that the search results are correctly displayed.

</details>

<details>
  <summary><b> :gear: Test Suite ★ Product Detail Page </b></summary>

TC ID 13 @ Verify Add to cart button is displayed. \
Objective: Validate the correct display of the "Add to Cart" button on the product detail page.

TC ID 14 @ Verify Product Category. \
Objective: Validate the correct display of a product's category on the product detail page.

TC ID 15 @ Verify Product Description. \
Objective: Validate the correct display of a product's description on the product detail page.

TC ID 16 @ Verify Product Description Header. \
Objective: Validate the correct display of the product description header on the product detail page.

TC ID 17 @ Verify Product Image. \
Objective: Validate the correct display of a product's image on the product detail page.

TC ID 18 @ Verify Product Price. \
Objective: Validate the correct display of a product's price on the product detail page.

TC ID 19 @ Verify Product Name. \
Objective: Validate the correct display of a product's name on the product detail page.

TC ID 20 @ Verify Product SKU. \
Objective: Validate the correct display of a product's SKU on the product detail page.

</details>

<details >
  <summary><b> :gear: Test Suite ★ Shopping Cart </b></summary>

TC ID 21 @ Remove Product from Cart. \
Objective: Add a product to the shopping cart, subsequently remove it, and confirm that the shopping cart is empty.

TC ID 22 @ Update Product Quantity in Cart. \
Objective: Adjust the quantity of an existing product in the shopping cart, both increasing and decreasing, and confirm that the shopping cart updates accurately reflecting the correct total price and quantity.


</details>

<details>
  <summary><b> :gear: Test Suite ★ Checkout </b></summary>

TC ID # @ TBD

</details>

<details>
  <summary><b> :gear: Test Suite ★ End-to-End Process </b></summary>

TC ID x1 @ Order as Guest User with "Cash on Delivery" option. \
Objective: Validate the successful completion of an order as a guest user with "cash on delivery" option, ensuring the process completes successfully.

TC ID x2 @ Order as Registered User "Cash on Delivery" option. \
Objective: Validate the successful completion of an order as a registered user with "cash on delivery" option, ensuring the process completes successfully.

TC ID x3 @ Order as Guest User with "Discount" coupon.  \
Objective: Validate the successful completion of an order as a guest user with a discount coupon, ensuring the process completes successfully.

TC ID x4 @ Order as Registered User with "Discount" coupon. \
Objective: Validate the successful completion of an order as a registered user with a discount coupon, ensuring the process completes successfully.

TC ID x5 @ Order multiple Products as Guest User with "Cash on Delivery" option. \
Objective: Validate the successful completion of an order with multiple products as a guest user with "cash on delivery" option, ensuring the process completes successfully.

TC ID x6 @ Order multiple Products as Registered User with "Cash on Delivery" option. \
Objective: Validate the successful completion of an order with multiple products as a registered user with "cash on delivery" option, ensuring the process completes successfully.

TC ID x7 @ Order multiple Products as Guest User with "Discount" coupon. \
Objective: Validate the successful completion of an order with multiple products as a guest user with a discount coupon, ensuring the process completes successfully.

TC ID x8 @ Order multiple Products as Registered User with "Discount" coupon. \
Objective: Validate the successful completion of an order with multiple products as a registered user with a discount coupon, ensuring the process completes successfully.

</details>


## Getting Started

To get started with MyStoreWebUI, follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the project's dependencies listed in the `requirements.txt` file using pip:

```bash
pip install -r requirements.txt
```


## To run the tests locally (default):

```
pytest -m tcid1

pytest -m end_to_end

pytest -m smoke

pytest -m regression
```

## Demonstration of a Successful End-to-End Test Case Execution:

This demonstration provides a practical example of how our automated tests validate the entire system, from start to finish, ensuring that all integrated components of the application function as expected.

![Selenium](https://raw.githubusercontent.com/DevTechMastery/images/main/gif/demo_store_selenium_python_test_e2e.gif)

## Jenkins Job: Configuring Launch Options

Jenkins, as a continuous integration system, plays a crucial role in our test automation framework. It allows us to schedule and automate the execution of our tests, ensuring that our application is continuously validated against our suite of tests.

Here are some possible configurations for setting up Jenkins jobs for our project:

1. **Scheduled Test Runs**: You can configure Jenkins to run the tests at specific times. This is useful for scheduling nightly builds or running tests during off-peak hours.

2. **Triggered Test Runs**: Jenkins can be configured to run tests in response to specific events, such as when code is pushed to the repository or when a pull request is created.

3. **Parameterized Test Runs**: You can set up Jenkins jobs that take parameters. This allows you to run the same set of tests with different configurations or test data.

4. **Parallel Test Runs**: Jenkins supports running jobs in parallel, which can significantly reduce the total test execution time when you have a large number of tests.

![Jenkins](https://raw.githubusercontent.com/DevTechMastery/images/main/screenshots/demo_store_selenium_python_jenkins.png)


## Allure Reports: Generation and Visualization
Allure Reports offer an elegant and user-friendly way to represent test results, making it easier to interpret and analyze test outcomes. The following steps guide you through the process of generating and viewing Allure Reports:

1. **Executing Tests with Allure Integration**: When executing your pytest tests, include the `--alluredir` option followed by the directory where you wish to store the Allure results. For instance:
```bash
# This command will run the regression tests and store the Allure results in the allure-results directory.
pytest -m regression --alluredir=allure-results
```
2. **Generate the Allure report:**:  After the tests have been executed, you can generate the Allure report using the Allure command line tool:
```bash
# This command generates the Allure report and automatically opens it in your default web browser.
allure serve allure-results
```

## Allure Report: Visualizing Test Status and Trends
Allure Reports not only provide a detailed overview of test status but also display trend graphs for a more comprehensive understanding of the test performance over time.

![Allure1](https://raw.githubusercontent.com/DevTechMastery/images/main/screenshots/demo_store_selenium_python_allure_report.png)

![Allure2](https://raw.githubusercontent.com/DevTechMastery/images/main/screenshots/demo_store_selenium_python_allure_grapths.png)

## Jira Integration: Attaching Test Results and Test Launch Details to Jira Tickets

Our testing framework is integrated with Jira, a widely-used issue tracking system. This integration allows us to attach test results and details of test launches directly to the corresponding Jira tickets. This feature enhances traceability and provides a comprehensive view of the testing process within the context of each issue.

The image below demonstrates a Jira ticket with attached test results and test launch details.

![Jira](https://raw.githubusercontent.com/DevTechMastery/images/main/screenshots/demo_store_selenium_python_jira.png)

## Slack: Real-Time Test Execution Notifications

Slack, as a real-time communication platform, plays a pivotal role in our test automation framework. It enables us to send instant notifications about the status of test executions, keeping the team updated about the progress and results of our testing efforts.

The image below illustrates a typical Slack notification generated by our testing framework.

![Slack](https://raw.githubusercontent.com/DevTechMastery/images/main/screenshots/demo_store_selenium_python_slack.png)