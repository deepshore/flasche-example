# flasche-example

This is an example dealing with how to use flasche

## Get the code

Clone this repo:
```bash
git clone https://github.com/deepshore/flasche-example
````

## Create and activate a virtual environment

Create a venv like this:

```bash
python3 -m venv venv
```

Activate the venv like this:

```bash
source venv/bin/activate
```

## Install flasche

Install flasche like this:

```bash
pip install flasche
```

## Build a project

Build a project like this:

```bash
flasche build example
```

## Run the project 

Run the app like this:

```bash
flasche run example
```

You can get the metrics here: [http://127.0.0.1:5000/metrics](http://127.0.0.1:5000/metrics).

Via the following link you can reach the swaggerUI: [http://127.0.0.1:5000/api/swagger](http://127.0.0.1:5000/api/swagger)

## Add an endpoint

Copy another_test_endpoint.py from this repo to example/endpoints:

```bash
cp another_test_endpoint.py example/endpoints/
```

Add the following line to the endpoints/__init__.py:

```python
from ..endpoints.another_test_endpoint import AnotherTestEndpoint
```

The new resource shows up after restarting the app.
