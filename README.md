# Py-One-Liners
* *Inspired by [tjf801](https://github.com/tjf801)*

For cool one-liners in the Python programming language **(eval() and exec() are cheating)** These are by no means meant to be efficient or fast, these are just for fun and to see if it's possible!

## Tricks:
* Pretty sure this is given, but use [lambdas](https://www.w3schools.com/python/python_lambda.asp) and [ternary conditionals](https://www.pythoncentral.io/one-line-if-statement-in-python-ternary-conditional-operator/)
* It's pretty hard to debug single line scripts, so use a handy dandy function that allows you to print a value and return it like this:
```
def debug(thing):
  print(thing)
  time.sleep(1)
  return thing
```
* List comprehension is probably going to be your friend.
* If you need to call a function in list comprehension you can do something like the below, which allows you to call a function in your list comprehension without messing up the contents of the finished list
```
[(i, print(i))[0] for in in range(10)]
```
* Yes, the `;` can be used in Python! A semicolon can be used to signify the end of a line. It, however, cannot be used inside sets of parentheses and brackets, but only at where the end of a line would be in regular Python. Example:
```
n = 2; [print(i) for i in range(n)]
```
* You can have optional arguments in your lambda functions just like in regular functions which you can use for temp variables, other lambda functions, or other useful things! Example:
```
(lambda thing=2: print(thing))
```
* Yes, you can do recursion with lambdas! Example:
```
f = lambda recurse, num: recurse(num-1) if num > 10 else num; f(f, 20)
```
