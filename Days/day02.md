# Day 2 – Python Script to check if the file or directory exists

Welcome to Day 2 of 99 Days of DevOps. On Day 1, we discussed about OS Module 

Now the main question is why you want to check if the file or directory exists?

Checking If the file exists or not is very important, as you want to make sure that file exists before you open it or before you are writing to that file, or before you overwrite that file. In Python, there are different ways to check whether the file exists, but I am going to cover three main topics

1- open()
2- os.path()
3- pathlib

## Approach 1:
Let start with open()

In your python console, try to open a non-existing file using open(). You will get a FileNotFoundError.
```bash
>>> open("abc.txt")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
'/tmp'
```

Try to open a file to which you don’t have permission. You can create a file and then change the permission via chmod.
```bash
touch filetest
chmod 100 filetest
ls -l filetest
---x------  1 plakhera  staff  0 Jun 27 16:50 filetest
```
Now in your Python console, try to open that file.
```bash
>>> open("filetest")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
PermissionError: [Errno 13] Permission denied: 'filetest'
```



