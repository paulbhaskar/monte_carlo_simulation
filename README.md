## Description

Monte Carlo Simulations

## Getting Started

### Installation

Install a python library globally on your machine called virtualenv <br>
Then follow the instructions here to create a virtual environment: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ <br>
Activate the virtual environment and install the python packages to the python virtual environment by running the following command: pip install -r requirements.txt

### Running unit tests

To run all tests, run the following command: pytest --run-slow <br>
To run fast tests, run the following command: pytest
To run tests for specific module, run the following command: pytest [PATH TO MODULE], ex: pytest poker/tests/texas_holdem_test.py <br>
To run tests for a specific test module in a module, run the following command: pytest [PATH TO MODULE]::[NAME OF CLASS], ex: pytest poker/tests/texas_holdem_test.py::TestPokerHandProbabilities --run-slow <br>
