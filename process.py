log_file = open("um-server-01.txt") # this opens the stored file and sets it to a variable


def sales_reports(log_file): # this starts a function
    for line in log_file: # this loops through the opened file
        line = line.rstrip() # this takes all the whitespace fom each line in the file
        day = line[0:3] # takes the first 4 elements of the row
        if day == "Mon": # if statement that tests if the value is === Tue
            print(line) # prints the result in the console

sales_reports(log_file) # invoking the function and passes in the open file in log_file