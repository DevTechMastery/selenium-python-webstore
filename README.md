## 📊 Test Automation Framework for the [Web Store](https://www.happyharbor.kesug.com/) Application

![logo.png](https://i.imgur.com/YKWONJp.png)


## Technology Stack
| <a href="https://www.python.org/"><img src="https://i.imgur.com/l1T2VxE.png" width="40" height="40"  alt="Python"/></a> | <a href="https://www.jetbrains.com/pycharm/"><img src="https://i.imgur.com/1rUVnJE.png" width="40" height="40"  alt="PyCharm"/></a> | <a href="https://docs.pytest.org/en/8.0.x/contents.html"><img src="https://i.imgur.com/eYAwneW.png" width="50" height="50"  alt="Pytest"/></a> |    <a href="https://www.selenium.dev/"><img src="https://i.imgur.com/m2aJGD9.png" width="40" height="40"  alt="selenium"/></a>     | <a href="https://faker.readthedocs.io/en/master/"><img src="https://i.imgur.com/027GEyk.png" width="40" height="40"  alt="Faker"/></a> | <a href="https://www.jenkins.io/"><img src="https://i.imgur.com/PYwxlPc.png" width="40" height="50"  alt="Jenkins"/></a> | <a href="https://www.docker.com/"><img src="https://i.imgur.com/oBfzO4R.png" width="45" height="45"  alt="Docker"/></a> |                                                                     <a href="https://github.com/"><img src="https://i.imgur.com/YMRfX5L.png" width="45" height="45"  alt="GitHub"/></a>                                                                     | <a href="https://allurereport.org/"><img src="https://i.imgur.com/AFfE03h.png" width="50" height="50"  alt="Allure"/></a> | <a href="https://slack.com/"><img src="https://i.imgur.com/NCfR0lb.png" width="40" height="40"  alt="Slack"/></a> |
|:-----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:| :---------: |:-------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                            Python                                                             |                                                                       PyCharm                                                                        |                                                                        Pytest                                                                        | Selenium |                                                            Faker                                                       |                                                             Jenkins                                                             |                                                             Docker                                                             |                                                                                              GitHub                                                                                                                                                         |                                                          Allure                                                           |                                                                         Slack                                                                         |

This project utilizes a variety of tools to achieve its automation goals:

* [Python](https://www.python.org/): The main programming language used for writing the test automation framework and tests.
* [PyCharm](https://www.jetbrains.com/pycharm/): An integrated development environment (IDE) used for writing and running the Python code.
* [Pytest](https://docs.pytest.org/en/latest/): A testing framework in Python, used for organizing and running the tests.
* [Selenium](https://www.selenium.dev/): A tool for automating web browsers, used for writing the UI tests.
* [Faker](https://faker.readthedocs.io/en/master/): is a Python library for generating fake data such as names, addresses, and phone numbers. It's useful for populating test data in automated tests.
* [Jenkins](https://www.jenkins.io/): A continuous integration system used to schedule and run the tests automatically.
* [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications in containers.
* [GitHub](https://github.com/): A version control system used for storing the project code and collaborating with team members.
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

The `webstore` test automation framework is built using a modern technology stack that includes Python, Selenium WebDriver, pytest, and Jenkins among others. This combination of technologies allows for robust, scalable, and maintainable automated testing of the web application's user interface.

## Repository Structure
The project structure is organized as follows:
```bash
myStoreWebUI/
├── src/
│   ├── pages/                      # Contains page objects
│   │   ├── home_page.py            # Page object for the home page
│   │   ├── my_account_page.py      # Page object for the my account page
│   │   ├── cart_page.py            # Page object for the cart page
│   │   ├── ...                     # Other page objects
│   │   └── locators/               # Contains locator classes
│   │       ├── AccountSignedIn.py  # Locator class for the account signed in page
│   │       ├── AccountSignedOut.py # Locator class for the account signed out page
│   │       ├── Cart.py             # Locator class for the cart page
│   │       └── ...                 # Other locator classes
│   ├── configs/                    # Contains configuration files
│   ├── helpers/                    # Contains helper scripts
│   └── seleniumextend.py           # Selenium extension file
├── tests/                          # Contains test cases
│   ├── home_page_tests/            # Test cases for the home page
│   ├── my_account_page_tests/      # Test cases for the my account page
│   ├── cart_page_tests/            # Test cases for the cart page
│   ├── checkout_page_tests/        # Test cases for the checkout page
│   ├── product_detail_page_tests/  # Test cases for the product detail page
│   └── ...                         # Other test cases
├── .gitignore                      # Specifies files and directories ignored by Git
├── conftest.py                     # Configuration file for pytest and fixtures setup
├── pytest.ini                      # Configuration file for pytest
├── requirements.txt                # Dependencies for the project
├── README.md                       # Documentation for the project
└── ...                             # Other project files

```

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
pytest -m tcid1                                       # Run a specific test case

pytest -m "tcid1 or tcid2 or tcid3"                   # Run multiple test cases

pytest -m "my_account or home_page or cart_page"      # Run test cases that belong to multiple test suites

pytest -m end_to_end                                  # Run all end-to-end test cases

pytest -m regression                                  # Run all regression test cases
```

## Demonstration of a Successful End-to-End Test Case Execution:

This demonstration provides a practical example of how our automated tests validate the entire system, from start to finish, ensuring that all integrated components of the application function as expected.

![Selenium](https://i.imgur.com/x0PbudD.gif)

## Jenkins Job: Configuring Launch Options

Jenkins, as a continuous integration system, plays a crucial role in our test automation framework. It allows us to schedule and automate the execution of our tests, ensuring that our application is continuously validated against our suite of tests.

Here are some possible configurations for setting up Jenkins jobs for our project:

1. **Scheduled Test Runs**: You can configure Jenkins to run the tests at specific times. This is useful for scheduling nightly builds or running tests during off-peak hours.

2. **Triggered Test Runs**: Jenkins can be configured to run tests in response to specific events, such as when code is pushed to the repository or when a pull request is created.

3. **Parameterized Test Runs**: You can set up Jenkins jobs that take parameters. This allows you to run the same set of tests with different configurations or test data.

4. **Parallel Test Runs**: Jenkins supports running jobs in parallel, which can significantly reduce the total test execution time when you have a large number of tests.

![Jenkins](https://i.imgur.com/yHKqenF.png)


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

![Allure1](https://i.imgur.com/D2TI1Ut.png)

![Allure2](https://i.imgur.com/TvvcOCR.png)

## Slack: Real-Time Test Execution Notifications

Slack, as a real-time communication platform, plays a pivotal role in our test automation framework. It enables us to send instant notifications about the status of test executions, keeping the team updated about the progress and results of our testing efforts.

The image below illustrates a typical Slack notification generated by our testing framework.

![Slack](https://i.imgur.com/fvr34Di.png)