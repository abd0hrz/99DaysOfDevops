Day 5 – A Python script to search files with specific extensions and get the file size

Welcome to Day 5of 101 Days of DevOps. The topic for today is a python script to search for a file with a specific extension(e.g., .txt, .jpeg) and then display the file size. These kinds of scripts are useful when you want to perform the cleanup operation or searching for a specific type of file.

On Day 1, we discussed OS Module. As part of the discussion, we discussed os.walk(). If you want to brush your concept, I am attaching the link; else, please check the above video if you directly want to go to the solution. https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-1-python-os-module/

On Day 3, we discussed the search for a file. This script is basically an extension of that https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-3-2/

As per Day 3, our code looks like this; in this code, we need to make a slight modification

import os

for dirpath, dirname, filename in os.walk("/etc/openldap"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == "hosts":
            print(comp_path)

To match the file with the specific extension, we will use the string method endswith(). Now the if condition will look like this

if file.endswith(".conf"):

To get the file size, we are going to use the os.path.getsize() method. This method checks the size of the specified path. It returns the size of the specified path in bytes.

file_size = os.path.getsize(comp_path)
print("File size is: ", file_size, "bytes")

So our final code will look like this

import os

for dirpath, dirname, filename in os.walk("/etc/openldap"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file.endswith(".conf"):
            print(comp_path)
            file_size = os.path.getsize(comp_path)
            print("File size is: ", file_size, "bytes")
