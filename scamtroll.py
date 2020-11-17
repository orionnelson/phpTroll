import requests
import os
import random
import string
import json
from english_words import english_words_set


special_chars = string.punctuation
uppers = string.ascii_uppercase
numbers = string.digits

chars = string.ascii_letters + string.digits + '!@#$%^&*'
random.seed = (os.urandom(1024))
endings =['@yahoo.com','@hotmail.com','@live.ca','@icloud.ca', '@gmail.com','@gmail.com','@gmail.com']



# CHANGE THIS LINE TO THE PHP POST PAGE OF SCAMMER
url = 'https://updatepaymentnetflix.bestcustomecentre.com/ajax/submit.php'
section = 'login'
names = json.loads(open('names.json').read())

def isvalid(string):
        scbool = list(map(lambda char: char in special_chars, string))
        ubool = list(map(lambda char: char in uppers, string))
        nbool = list(map(lambda char: char in numbers, string))
        if any(scbool):
                scb=True
        else:
                scb=False
        if any(ubool):
                ub=True
        else:
                ub=False
        if any(nbool):
                nb=True
        else:
                nb=False
        return (scb and ub and nb)
        
        


def genpass():
        password = ''.join(random.sample(english_words_set,random.randint(1,3)))
        extra = ''.join(random.choice(chars) for j in range (random.randint(2,3)))
        password = password + extra
        return password
        

for name in names:
        
        name_extra = ''.join(random.choice(string.digits))
        username = name.lower() + name_extra + random.choice(endings)
        password = genpass()
        # UPPER CASE LOWERCASE AND SPECIAL CHARACTER AND 6 < LENGTH < 16 
        while(len(password) > 18 or len(password) < 7 or ( not isvalid(password))):
                password = genpass()
        #The Post method visit the page using VPN and enter bs email into feilds inpect element first go to Network
        # Check Preserve Log
        # For example enter test@gmail.com  :  Password123* and press submit
        # Look at the network data for an page ending in php
        # If you find it the post data feilds and url look like this https://ibb.co/BsN61T9 this is your url and post fields
        requests.post(url, allow_redirects=False, data={
                'section': section,
                'email': username,
                'pass': password
        })

        print ('sending username:  ' +username + ' and password:  ' + password)
