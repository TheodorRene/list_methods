# list_methods
Tired of not having map, filter and reduce easily available like in
Javascript, Java, Kotlin, etc? Fear not, this is the package for you.

# Installation
[![PyPI version](https://badge.fury.io/py/list-methods.svg)](https://badge.fury.io/py/list-methods)

```
pip install list_methods
```

# Use
```
>>> from list_methods import L
>>> l = L([1,2,3])
>>> plusone = lambda x : x+1
>>> greater_than_noe = lamda x : x > 1
>>> l.map(plus_one).c()
[2,3,4]
>>> l.filter(greater_than_one).c()
[2,3]
>>> l.map(plus_one).map(plus_one).filter(greater_than_one).c()
[3,4,5]
>>> agg_plus = lambda x,y: x+y
>>> l.reduce(agg_plus)
6
```

# Gotchas
Remember to call the .c() method since this resets the object so it can be used
further. This is not necessary when ending the pipeline with .reduce()

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
[2,3,4]
>>> l.map(plus_one)
[3,4,5]
```

# TODO
* Write tests
* Write benchmarks
