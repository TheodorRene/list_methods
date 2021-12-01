# list_methods [Experimental]
Tired of not having map, filter and reduce easily available like in
Javascript, Java, Kotlin, etc? Fear not, this is the package for you(sort of). 

Experimental package adding .map(), .filter() and .reduce() as list methods.
Made mostly as PoC showing how the Python language can be extended in some way. 

# Installation
[![PyPI version](https://badge.fury.io/py/list-methods.svg)](https://badge.fury.io/py/list-methods)

```
pip install list_methods
```

# Use
```
>>> from list_methods import L
>>> l = L([1,2,3])
>>> plus_one = lambda x : x+1
>>> greater_than_one = lamda x : x > 1
>>> l.map(plus_one).c()
L([2,3,4])
>>> l.filter(greater_than_one).c()
L([2,3])
>>> l.map(plus_one).map(plus_one).filter(greater_than_one).c()
L([3,4,5])
>>> agg_plus = lambda x,y: x+y
>>> l.reduce(agg_plus)
6
```

# Gotchas
Remember to call the .c() method since this resets the object so it can be used
further. This is not necessary when ending the chain of operations with .reduce()

## Javascript

```
> l = [1,2,3]
> l.map(x => x +1)
[2,3,4]
> l.map(x => x +1)
[2,3,4]
```


## list_methods - Python

```
>>> l.map(plus_one)
L([2,3,4])
>>> l.map(plus_one)
L([3,4,5])
```

## Gotcha #2
* The list needs to be copied when instantiating the object so it can be reset for other use. In the future one should maybe add a flag to skip this list copy if the list is only used in one place.  

# TODO
* Write tests
* Write benchmarks
* Test a implementation where a new instance of the class is returned instead of self
