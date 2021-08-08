Firstly, understand that when you run a file, the variable __name__ in that file will be "__main__" regardless of the name of the file. Also note that __name__ is a variable which is local to each file.

So let's write a file called test_2.py, and we want to be able to test it in isolation before we incorporate it into our main program.
```
def foo(x):
    print(f"Foo{x}!")
 
foo("test")
```
The output is
```
Footest!
```
Good. The program works. Let's call it from main.py:
```
from test_2 import foo
 
foo("bar")
```
The output is
```
Footest!
Foobar!
```
Oh dear. Why is that Footest! printing?

That's because when you import a file, the interpreter will run it!

So let's alter the file test_2.py:
```
def foo(x):
    print(f"Foo{x}!")
 
print(f'{__name__ = }')  # I've added this so that you can see what happens.
if __name__ == "__main__":
    foo("test")
```
Now we can test it in isolation, where __name__ will be "__main__", and we can also call it from main.py, where __name__ will be "test_2" (and hence the function doesn't get called during the import).