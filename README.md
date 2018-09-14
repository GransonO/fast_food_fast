# fast_food_fast
A food delivery web application aimed at testing my understanding of HTML, CSS and Javascript... Languages necessary fro the web development challenges

[![Build Status](https://travis-ci.com/GransonO/fast_food_fast.svg?branch=develop)](https://travis-ci.com/GransonO/fast_food_fast)

[![Coverage Status](https://coveralls.io/repos/github/GransonO/fast_food_fast/badge.svg?branch=develop)](https://coveralls.io/github/GransonO/fast_food_fast?branch=develop)

[![Test Coverage](https://api.codeclimate.com/v1/badges/21af8073dc13173e9504/test_coverage)](https://codeclimate.com/github/GransonO/fast_food_fast/test_coverage)

# Flask Server Implementation
### What should be implemented
#### Server-Side Framework: <Flask Python Framework>
#### Linting Library: <Pylint, a Python Linting Library>
#### Style Guide: <PEP8 Style Guide>
#### Testing Framework: <PyTest, a Python Testing Framework>
### Guidelines to be followed
Use pivotal tracker tool to create user stories to setup and test API endpoints that do the following using data structures
#### Place a new order for food.
#### Get a list of orders.
#### Fetch a specific order.
#### Update the order status.
Ensure tasks entered are feature, bug or chore
Setup the server side of the application using the flask framework
Setup linting library and ensure that your work follows the specified style guide requirements
Setup test framework
Using separate branches for each feature, create version 1 (v1) of your RESTful API to power front-end pages
At minimum, you should have the following API endpoints working:
       
### EndPoint Functionality
#### GET /orders
Get all the orders.
#### GET /orders/<orderId>
Fetch a specific order
#### POST /orders
Place a new order.
#### PUT /orders/<orderId>
Update the status of an order.

Write tests for the API endpoints
Ensure to test all endpoints and see that they work using Postman.
Integrate TravisCI for Continuous Integration in your repository (with ReadMe badge).
Integrate test coverage reporting (e.g. Coveralls) with badge in the ReadMe.
Obtain CI badges (e.g. from Code Climate and Coveralls) and add to ReadMe.
Ensure the app gets hosted on Heroku.
