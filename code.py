# First Instal Libraries 
# pip3 install socket
# pip3 install ip2geotools

import socket

from ip2geotools.databases.noncommercial import DbIpCity

# here you can enter any website url address
WebsiteName = input("Insert Website URL : ")

# they fetch ip address
WebsiteIP = socket.gethostbyname(WebsiteName)

response = DbIpCity.get(WebsiteIP,api_key='free')

# Then showing information about any website
print("IP: ",ip)

print("City: ",response.city)

print('Region: ',response.region)

print("Country: ",response.country)
