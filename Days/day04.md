# Day 4 – A Python script to search files greater than X days old

Welcome to Day 4 of 99 Days of DevOps. The topic for today is a python script to search for a file greater than X days old. As a DevOps/System Administrator, this is one of the common tasks we encounter as a part of our daily job. This kind of script is helpful when your server is low in disk space and needs to search for older files and then delete them.

So far, our code looks like this, whereby using os.walk(), we are iterating over the /etc directory and then using os.path.join() we combine directory with the filename.

Once we get the complete path, the next step is to find when the particular file is created to do that with the time help of os.path.getctime(filename).

But the output of the above command is in sec. Now it’s time to introduce a new Python module called datetime. Using datetime, we can convert this time second into the local date corresponding to the POSIX timestamp using datetime.datetime.fromtimestamp() and later save that into a variable file_creation_time.

So far, our code looks like this.

Now we have the date on which the file is created; the next step is to find the current date. Finding current dates is pretty easy in the datetime module, and we can do that by using datetime.datetime.now(). Save the output of the below command in variable today_date.

The next step is to calculate the difference between the current date and the file creation date and use days() to get only the days.

Now depending upon your requirement, use if condition to get the files, e.g., 15 days, and print the output

So your complete code will look like this
