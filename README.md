# Python-Unit-Tests

> Look at the test and the original assignment: 

>Write unit test code to test a python method which will split URLs into their pieces
>The function will take a string as a parameter, it should return the following:
> - A list with 
>   - The protocol string
>   - The the server name
>   - The path
>   - Any arguments (possibly empty)
>   - Malformed URLs will return an empty list.

> Write a paragraph evaluating the test case. Does the test case you are evaluating accurately formalize the written requirements? In what way is it accurate or not? (your writing must be report/paper quality writing)
> Write split url code which will pass the test you have been given.


```Python
__author__ = 'SWarren'
from urllib.parse import urlparse

class Urlsplit:
    def SplitIntoList(self,address):
        o = urlparse(address)
        if o.scheme or o.netloc != '':
            urlList = [o.scheme,o.netloc,o.path,o.query]
            return urlList
        else:
            return 'error in input'
```

## The Unit Testing

![The Unit Testing](https://raw.githubusercontent.com/SMWARREN/Python-Unit-Tests/master/images/testcase.png)

>he Python unit testing framework, sometimes referred to as “PyUnit,” is a Python language version of JUnit, by Kent Beck and Erich Gamma. JUnit is, in turn, a Java version of Kent’s Smalltalk testing framework. Each is the de facto standard unit testing framework for its respective language.
