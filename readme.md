# API Automation Testing with Pytest
## Description
This project is a simple replication of the course '[Postman Beginner's Course-API Testing](https://www.youtube.com/watch?v=VywxIQ2ZXw4),' from [freeCodeCamp](www.freecodecamp.org). 

Pytest is used as the test runner in this project. Python requests library is used to get the http response from API endpoint.

## How to
### Install 
This program uses python 3.10.0, however the minimum requirement of Pytest is Python 3.7, so, it can be downloaded from Python [website](https://www.python.org/downloads/).

If using the same python version, the Pytest and requests libraries can be installed with this command:
##### Windows Console
```console
C:\{Your Directory}\TestDir>python -m pip install requirements.txt
```
##### Unix Console
```console
machine@username~$ python3 -m pip install requirements.txt
```

If using different python version, Pytest installation can be found in [pytest website].(pytest.org)

### Run the Project

Clone the repo with Git to your desired local machine directory:
```Git
git clone [url]
```

Run the test with the following command:
##### Windows Console
```console
C:\{Your Directory}\TestDir>pytest test_happy_path.py
```
##### Unix Console
```console
machine@username~$ pytest test_happy_path.py
```

## Resource
You could find the API documentation below:
[Simple-Book-Api](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)