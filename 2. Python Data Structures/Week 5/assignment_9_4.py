"""
9.4 Write a program to read through the mbox-short.txt and 
figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines 
as the person who sent the mail. The program creates a Python dictionary that 
maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using 
a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Could not read file")
    quit()

mail_dict = {}

for line in handle:
    # Getting the sender info
    if line.startswith('From:'):
        line = line.split()
        # Capturing the e-mail part
        dict_key = line[1]
        # Dictionary operation
        if dict_key not in mail_dict:
            mail_dict[dict_key] = 1
        else:
            mail_dict[dict_key] += 1
    else:
        continue

# Sorting dictionary according to their values
sorted_dict = sorted(mail_dict.items(), key=lambda kv: kv[1])
length = len(sorted_dict)
print("{} {}".format(sorted_dict[length-1][0], sorted_dict[length-1][-1]))

# ? How do I sort a dictionary by value?
#! https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

# ? Reverse / invert a dictionary mapping
#! https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
