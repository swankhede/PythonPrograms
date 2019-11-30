import socket
import requests
url = "http://mu.ac.in/portal/wp-content/uploads/2014/11/1T033121.pdf"
res = requests.get(url)
print(res)
f = open("timetable.pdf","wb")
f.write(res.content)
f.close()