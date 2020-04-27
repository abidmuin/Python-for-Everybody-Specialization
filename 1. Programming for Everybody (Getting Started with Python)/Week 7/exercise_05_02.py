"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

"""
Desired Output
Invalid input
Maximum is 10
Minimum is 2
"""


largest = None
smallest = None
num_list = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        num_list.append(num)
    except:
        print('Invalid input')
        continue

list.sort(num_list)
smallest = num_list[0]
largest = num_list[-1]

print("Maximum is {}".format(largest))
print("Minimum is {}".format(smallest))
