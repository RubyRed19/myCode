#!/usr/bin/env python3

#list containing 3 items
my_list = [ "192.168.0.5", 5060, "UP" ]
iplist =  [5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh' ]
#show first item
print("The first item in the list (IP): " + my_list[0] )

#show the last item in the list
print("The last item in the list (state): " + my_list[2] )

# display IP addresses
print(f"IP addresses: {iplist[3]}, {iplist[4]}")
