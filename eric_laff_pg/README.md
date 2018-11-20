# TICKLE Life Insurance MVP by Eric Laff
    
        
## Design Choice

My goal with this application was to make it as dynamic and extensible as possible. I thought
of this as taking a web api in the future so my design choice is reflected in the way the class takes in arguments. Hence my choice to set up the health condition rates in a dictionary to replicate a json payload that had been processed. I chose to create a class and instantiate a new instance each time. So in theory for multiple rates for different customers, say if we decided to add others to the plan. I also thought it to be possible to add another attribute to the class that allows for other member for instance, an array or dictionary. The addition of the different methods within the class allows for different uses if needed in the future within the engine.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Homebrew
Pip

### Installing

A step by step series of examples that tell you how to get a development env for Python

To install Homebrew, open Terminal or your favorite OSX terminal emulator and run
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
The script will explain what changes it will make and prompt you before the installation begins. Once you’ve installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. You can do this by adding the following line at the bottom of your ~/.profile file
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```
Now, we can install Python 3:
```
$ brew install python
```
This will take a minute or two.

For Running the Test install pytest
```
pip3 install pytest pytest-cache
```
## Running the tests

To run all tests
cd tickle_mvp
```
pytest rate_calculator_test.py
```
```
=============================  rate_calculator_test.py  ==============================

---------------------------------------------------------------------

Ran 3 tests in 0.000s

OK
```

### Break down into end to end tests

Each test tests different customers information. The test makes sure each rate is generated
correctly. It also checks that the age is over 18 by returning a bool. 

```
    def test_brad_rate(self):
        rates = dict(allergies="0.01", sleep_apnea='0.06', heart_disease='0.17')
        brad = CustomerRate(name="Brad", age="20", gender="male", health_condition="heart_disease", base_cost=100 , condition_rates=rates)

        self.assertEqual(brad.check_age, True)
        self.assertEqual(brad.annual_rate(), 117.00)
```

As an added bonus I created a small file thatsort of pretty prints an insurance quote
to demonstrate the ease of use with the class.

rate_summary.py
```
python rate_summary.py
```

## Built With

* [Python](https://www.python.org/) - The language used


## Authors

* **Eric Laff**



