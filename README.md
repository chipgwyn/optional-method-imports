Question:
  Can I import functions from another file into my class.
  
Answer: Yep!

The basics are:
http://www.qtrac.eu/pyclassmulti.html

```
# DataStore.py

import _DataStore

class DataStore(_DataStore.Mixin): # Could inherit many more mixins

    def __init__(self):
        self._a = 1
        self._b = 2
        self._c = 3

    def small_method(self):
        return self._a
```
Our mixin classes must not have an __init__ or store any data—but they have full access to self and its data of course.

```
# _DataStore.py

class Mixin:

    def big_method(self):
	    return self._b

    def huge_method(self):
	    return self._c
```

See the included files.

t.py has a "User" class which has stuff inherited from our base "Model" class
and also any functions from "funcs".

