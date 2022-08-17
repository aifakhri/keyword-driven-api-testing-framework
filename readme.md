# Keyword Driven API Automation Testing Framework
## Description
This is a Keyword-driven API automation testing framework that is built on top of Pytest. It is built by following Page Object Model design pattern to make a modular test framework. 

### Test Case
This framework test cases are for functional testing, and there are [positive (happy)](https://docs.google.com/spreadsheets/d/14vKRTYoAHq3N-eRT_F0lG1cYMGvemRwvwseaaezhLaY/edit?usp=sharing) and [negative (sad)](https://docs.google.com/spreadsheets/d/1E2gCpBsI8c-WNf-0s-RderDmBYs6fieR1cjxIIZ9cAo/edit?usp=sharing) testing path for each API endpoint. 

## How to
### Install 
This program uses python 3.10.0, however the minimum requirement for Pytest is Python 3.7. so, it can be downloaded from Python [website](https://www.python.org/downloads/).

If using the same python version, the Pytest and requests libraries can be installed with this command:
```console
C:\{Your Directory}\TestDir>python -m pip install requirements.txt
```

### Run the Project
Clone the repo with Git to your desired local machine directory:
```Git
git clone [url]
```
There are several ways to run this program

##### Running All the Tests
To run all the test suites in the modole
```Console
pytest
```
##### Running Only Positive Tests
```Console
pytest -k test_positive
```
##### Running Only Negative Tests
```Console
pytest -k test_negative
```
##### Running Only Endpoint (book, order or ApiClient)
```Console
pytest -k {{ endpoint name }}_endpoint
```
For example if you want to test only book endpoint (both negative and positive):
```Console
pytest -k book_endpoint
```
##### Note: 
You will encounter error in the testing negative test. This is expected behaviour because the API is designed to for testing. Hence, we prove error on the API endpoint!
If you have an error with API Client, please note that you can only request client once per seven day. So, if on the positve and negative test for apiClient, you might get inconsistent value.

## Resource
You could find the API documentation below:
[Simple-Book-Api](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)