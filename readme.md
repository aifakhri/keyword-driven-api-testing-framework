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
The ``program_runner.py`` file will run all the test cases inside the ``test_cases`` folder by running this command:
```Windows Console
python program_runner.py
```

You could also select whether you want to run positive (happy) or negative (sad) test cases in the ``test_cases`` folder by adding ``-t`` option while running the ``program_runner.py`` file. Here is the example:
```Windows Console
python program_runner.py -t positive
```

Note: the argument is only positive or negative. Other will be rejected.

## Resource
You could find the API documentation below:
[Simple-Book-Api](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)