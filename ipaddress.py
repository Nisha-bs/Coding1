#!/usr/bin/python3

class Solution:
    def IPaddress(address):
        
        defanged_version = address.replace(".", "[.]")
        print(defanged_version)
Solution.IPaddress("1.1.1.1")
