import inspect

for function in inspect.getmembers(inspect, inspect.isfunction):
    print inspect.getargspec(function[1])
