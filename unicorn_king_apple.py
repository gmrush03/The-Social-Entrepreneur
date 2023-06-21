#The Social Entrepreneur 

#This program is designed to help social entrepreneurs interested in starting their own business. 

#Importing modules 
import json
import requests
import time
import webbrowser

#Defining our initial variables 
social_entrepreneurs_data = {}

#Prompting the user to enter their name 
name = input("What's your name? ")

#Printing out a greeting to the user
print("Hello " + name + "! Good to have you here. Let's find you some resources to help you get started in the world of social entrepreneurship!")

#Retrieving the most popular social entrepreneur resources from the web
response = requests.get("https://www.forbes.com/top-social-entrepreneurs")

#Parsing the response from the website 
data = json.loads(response.text)

#Iterating through the data to add it to our dictionary
for item in data['entrepreneurs']:
	social_entrepreneurs_data[item['name']] = item

#Printing out the resources found
print("We found these top resources for social entrepreneurs:")
for name in social_entrepreneurs_data:
	print(name)

#Prompting the user to select a resource they would like to explore
resource_choice = input("Which resource would you like to explore? ")

#Creating a URL for the resource 
url = social_entrepreneurs_data[resource_choice]['url']

#Opening the resource in a new tab 
webbrowser.open_new_tab(url)

#Waiting for 5 seconds
time.sleep(5)

#Printing out a message for the user
print("Thanks for using The Social Entrepreneur! We wish you the best of luck in your journey and hope that you find something that helps you get your business started!")