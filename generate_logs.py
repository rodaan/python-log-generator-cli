#!/usr/bin/python

# author: rodaan - 04/17/2017
# This is python script generates fake log files --> made for stress testing logging collectors
# Takes two or more arguments:
# 1: number of logs to generate
# 2 and more: file append logs to

# Example Log:
# 2017-04-14T14:59:48.817083Z: level=similique, s=hic, component=doloribus, host=ayers-nguyen.com, parent-id=9, span-id=8, trace-id=8, pid=6372, fileName=fugiat.avi, lineNo=566442279, msg="Cumque illum officiis cumque harum perferendis totam nostrum."

import datetime
from sys import argv
from faker import Factory
fake = Factory.create()

if len(argv) - 2 < 3:
    print("This is python script generates fake log files --> made for stress testing logging collectors")
    print("Must take two or more arguments:")
    print("1: number of logs to generate")
    print("2 and more: file append logs to")
    quit()

numOfLogs = int(argv[1])

print("Generating logs...")
print("Number of files to generate logs for: ",  len(argv) - 2)
print("Files appended: ", argv[2:])

for i in range(0, numOfLogs):
    time = datetime.datetime.now()
    
    for j in range(2, len(argv)):
        with open(argv[j], "a") as myfile:
            myfile.write(time.isoformat() + "Z: level=" + fake.word() + ", s=" + fake.word() + ", component=" +fake.word() + ", host=" + fake.domain_name() + ", parent-id=" + str(fake.random_digit_not_null()) + ", span-id=" + str(fake.random_digit_not_null()) + ", trace-id=" + str(fake.random_digit_not_null()) + ", pid=" + str(fake.random_int(min=1000, max=9999)) + ", fileName=" + fake.file_name(category=None, extension=None) + ", lineNo=" + str(fake.random_number(digits=None, fix_len=False)) + ", msg=\"fake.sentence(nb_words=6, variable_nb_words=True)\"\n") 


print("Logs generated!")
