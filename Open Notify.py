import requests

# Getting the file using GET method which gets the link of the API
response = requests.get("http://api.open-notify.org/astros.json")

# if prints 200: success or else failure
# print("Status code : ", response.status_code)

# The API gives back json file
jsonData = response.json()

'''
This is the structure of json file that you may get

{'people': [{'name': 'Christina Koch', 'craft': 'ISS'}, 
			{'name': 'Alexander Skvortsov', 'craft': 'ISS'}, 
			{'name': 'Luca Parmitano', 'craft': 'ISS'}, 
			{'name': 'Andrew Morgan', 'craft': 'ISS'}, 
			{'name': 'Oleg Skripochka', 'craft': 'ISS'}, 
			{'name': 'Jessica Meir', 'craft': 'ISS'}],
'number': 6, 
'message': 'success'}


From above we can conclude that there are 3 keys 'people','number',and 'message'. 
key 'people' has dictionary enclosed within a list
'''

# Finding number of people aboard
noOfPeople = jsonData['number']
print("Number of people : ", noOfPeople, "and they are ")

# Finding names and the crafts they are in
peopleDetails = jsonData['people']
names = []
crafts = []
for i in range(0, len(peopleDetails)):
    names.append(peopleDetails[i]['name'])
    crafts.append(peopleDetails[i]['craft'])

# Prints names and crafts
for i in range(0, len(names)):
    print("Name : ", names[i], " in Craft : ", crafts[i])
