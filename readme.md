# Keyword Driven API Automation Testing Framework
## Description
This is a Keyword-driven API automation testing framework that is built on top of Pytest. It is built by following Page Object Model design pattern to make a modular test framework. 

## How to
### Install 
This program uses python 3.10.0, however the minimum requirement of Pytest is Python 3.7, so, it can be downloaded from Python [website](https://www.python.org/downloads/).

If using the same python version, the Pytest and requests libraries can be installed with this command:
```console
C:\{Your Directory}\TestDir>python -m pip install requirements.txt
```

If using different python version, Pytest installation can be found in [pytest website.](pytest.org).

### Run the Project

Clone the repo with Git to your desired local machine directory:
```Git
git clone [url]
```

Run the test with the following command:
##### Windows Console
```console
C:\{Your Directory}\TestDir>pytest test_validation_api.py
```

## Resource
You could find the API documentation below:
[Simple-Book-Api](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)

And for more detail explanation on how to build this framework, please check out my medium [story]()