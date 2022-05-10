# Day 3 – A python script to search for a file

Welcome to Day 3 of 99 Days of DevOps. The topic for today is a python script to search for a file. As a DevOps/System Administrator, this is one of the common tasks we encounter as a part of our daily job. The idea behind it is to create a find utility using Python to pass directory names and files to search.

So far, our code looks like this, whereby using os.walk(), we are iterating over the /etc directory and then using os.path.join() we combine directory with the filename.

To find out the specific file, we can use the if statement and then only print the complete path if the file matches.

So our complete code will look like below.

If you save this code in find_files.py and search for hosts file in /etc directory, you will get the below output.

The second version of this script is to make it user-friendly so that it will accept arguments like the path to search(e.g.,/etc.) and then filename(hosts) on the command line; we will achieve that with the help of the argparser module.

These are the steps you need to follow to use argparse

1. Import the Python argparse library

2. Create the parser

3. Add optional and positional arguments to the parser. Here we are passing two-argument pathname to specify the path and filesearch for the file to search.

4. Execute .parse_args()

If you execute your script with the -h(help) option, you will get the output below.

Now you need to make few changes to your code. Rather than passing /etc to os.walk(), you need to pass args.pathname, and similarly, rather than passing filename directly, i.e., hosts, you need to pass args.filesearch.

To execute your script.
