# Day 4 – A Python script to search files greater than X days old

Welcome to Day 4 of 99 Days of DevOps. The topic for today is a python script to search for a file greater than X days old. As a DevOps/System Administrator, this is one of the common tasks we encounter as a part of our daily job. This kind of script is helpful when your server is low in disk space and needs to search for older files and then delete them.

So far, our code looks like this, whereby using os.walk(), we are iterating over the /etc directory and then using os.path.join() we combine directory with the filename.
```python
import os
 ```
```python
for dirpath, dirname, filename in os.walk("/etc"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
 ```
 
Once we get the complete path, the next step is to find when the particular file is created to do that with the time help of os.path.getctime(filename).
```python
>>> os.path.getctime("/etc/hosts")
1623687666.8315635
 ```
 
But the output of the above command is in sec. Now it’s time to introduce a new Python module called datetime. Using datetime, we can convert this time second into the local date corresponding to the POSIX timestamp using datetime.datetime.fromtimestamp() and later save that into a variable file_creation_time.
```python
datetime.datetime.fromtimestamp(os.path.getctime("/etc/hosts"))
datetime.datetime(2021, 6, 14, 9, 21, 6, 831563)
 ```
 
So far, our code looks like this.
```python
import os
import datetime


for dir,dirpath,filename in os.walk("/var/log"):
    for file in filename:
        complete_path=os.path.join(dir,file)
        file_creation_time=datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
 ```
 
Now we have the date on which the file is created; the next step is to find the current date. Finding current dates is pretty easy in the datetime module, and we can do that by using datetime.datetime.now(). Save the output of the below command in variable today_date.
```python
>>> datetime.datetime.now()
datetime.datetime(2021, 7, 4, 10, 31, 41, 664467)
 ```
 
The next step is to calculate the difference between the current date and the file creation date and use days() to get only the days.
```python
time_diff=(today_date-file_creation_time).days
 ```
 
Now depending upon your requirement, use if condition to get the files, e.g., 15 days, and print the output
```python
file_age=15
if time_diff> file_age:
    print(complete_path, time_diff)
 ```
So your complete code will look like this

```python
import os
import datetime

file_age=15
today_date=datetime.datetime.now()

for dir,dirpath,filename in os.walk("/var/log"):
    for file in filename:
        complete_path=os.path.join(dir,file)
        file_creation_time=datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
        time_diff=(today_date-file_creation_time).days
        if time_diff> file_age:
            print(complete_path, time_diff)
 ```
 
