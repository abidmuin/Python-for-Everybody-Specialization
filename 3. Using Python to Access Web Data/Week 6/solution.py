import json
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
    exit()

else:
    print("Retrieving " + str(address))
    response = urllib.request.urlopen(address)
    data = response.read()
    print('Count: ' + str(len(data)))
    info = json.loads(data)
    # ? 'result' is a list type
    result = info["comments"]

    index = 0
    total = 0
    length = len(result)
    while (length != 0):
        temp = result[index]["count"]
        total += temp
        index += 1
        length -= 1
    print('Sum: ' + str(total))
