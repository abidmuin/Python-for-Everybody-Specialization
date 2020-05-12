import xml.etree.ElementTree as ET
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
sum_result = 0

address = input('Enter location: ')
if len(address) < 1:
    exit()

else:
    print("Retrieving " + str(address))
    response = urllib.request.urlopen(address).read()
    tree = ET.fromstring(response)

    for number in tree.findall('.//count'):
        result = int(number.text)
        sum_result += result
        count += 1
    print("Count: " + str(count))
    print("Sum: " + str(sum_result))
