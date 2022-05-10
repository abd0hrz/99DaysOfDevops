# Day 3 – A python script to search for a file

Welcome to Day 3 of 99 Days of DevOps. The topic for today is a python script to search for a file. As a DevOps/System Administrator, this is one of the common tasks we encounter as a part of our daily job. The idea behind it is to create a find utility using Python to pass directory names and files to search.

So far, our code looks like this, whereby using os.walk(), we are iterating over the /etc directory and then using os.path.join() we combine directory with the filename.
```bash
import os

for dirpath, dirname, filename in os.walk("/etc"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
 ```

To find out the specific file, we can use the if statement and then only print the complete path if the file matches.
```bash
if file == "hosts":
    print(comp_path)
```
So our complete code will look like below.
```bash
import os

for dirpath, dirname, filename in os.walk("/etc"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == "hosts":
            print(comp_path)
```
If you save this code in find_files.py and search for hosts file in /etc directory, you will get the below output.
```bash
python3 find_files.py           
/etc/hosts
```

The second version of this script is to make it user-friendly so that it will accept arguments like the path to search(e.g.,/etc.) and then filename(hosts) on the command line; we will achieve that with the help of the argparser module.

These are the steps you need to follow to use argparse

1. Import the Python argparse library
```bash
import argparse
```
2. Create the parser
```bash
my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
```
3. Add optional and positional arguments to the parser. Here we are passing two-argument pathname to specify the path and filesearch for the file to search.
```bash
my_parser.add_argument("pathname",
```
```bash
help='Please enter the directory path ')
```
```bash
my_parser.add_argument("filesearch",
```
```bash
help='Please enter the filename to search')
```

4. Execute .parse_args()
```bash
args = my_parser.parse_args()
```

If you execute your script with the -h(help) option, you will get the output below.
```bash
python3 find_files.py -h
usage: find_files.py [-h] pathname filesearch
```

```bash
Reading the directory path to find the file
```

```bash
positional arguments:
  pathname    Please enter the directory path
  filesearch  Please enter the filename to search
```

```bash
optional arguments:
  -h, --help  show this help message and exit
```

Now you need to make few changes to your code. Rather than passing /etc to os.walk(), you need to pass args.pathname, and similarly, rather than passing filename directly, i.e., hosts, you need to pass args.filesearch.
```python
for dirpath, dirname, filename in os.walk(args.pathname):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == args.filesearch:
            print(comp_path)
```

To execute your script.
```bash
python3 find_files.py /etc hosts
/etc/hosts
```

