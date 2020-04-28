"""
10.2
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Could not read file")
    quit()

dict_time = {}

for line in handle:
    if (line.startswith('From')) and not (line.startswith('From:')):
        line = line.split()
        time = line[5]
        hour = time[:2]
        if hour not in dict_time.keys():
            dict_time[hour] = 1
        else:
            dict_time[hour] += 1

# Sorting dictionary according to their keys
sorted_dict = sorted(dict_time.items(), key=lambda kv: kv[0])
length = len(sorted_dict)

for k, v in sorted_dict:
    print('{} {}'.format(k, v))
