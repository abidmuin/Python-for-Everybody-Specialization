import re

pattern = "[0-9]+"
total = 0

try:
    with open('3. Using Python to Access Web Data\Week 2\/regex_sum_484093 (test dataset).txt', 'r') as f:
        for line in f:
            line = line.strip()
            data = re.findall(pattern, line)
            for num in data:
                total += int(num)

except:
    print("Could not read the file!")
    quit()

print(total)
