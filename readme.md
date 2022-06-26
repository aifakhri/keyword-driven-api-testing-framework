#Automation API Testing with Pytest
##Introduction
This project is a simple replication of the course '[Postman Beginner's Course-API Testing](https://www.youtube.com/watch?v=VywxIQ2ZXw4),' from [freeCodeCamp](www.freecodecamp.org). 

However, pytest is used to automate the testing instead of postman, and python requests library to get the http response from the end point. 

In the future, a Sad-path testing method with modular approach, which is not covered on the course, will be added.

##Project

The current project consists of a simple pytest structure with conftest.py, which contain fixtures to make the project cleaner. 

To run the test use this command from command line on the test directory:

######Windows cmd
```console
C:\Users\HostUsername\Document\TestDir>pytest test_book_api
```
######Unix/Linux Shell
```console
machine@username~$ pytest test_book_api
```

##Resource
You could find the API documentation below:
[Simple-Book-Api](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)