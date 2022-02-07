import requests
import json

class2022 = "Y2lzY29zcGFyazovL3VzL1JPT00vN2Q1MWU5ODAtNzM3OS0xMWVjLWJiNWItMTU4YzlkMDU0YmI5"

Headers = {
    "Authorization" : "Bearer ZWJjMzJhZTQtMTNjZS00ZTgxLWJmZjWViMjcyOTk1MjQxZWQ3NzYtMjJh_PF84_1eb6f43-417f-9974-ad72cae0e10f", 
    "Content-Type" : "application/json"
    }

response = requests.post("https://webexapis.com/v1/messages",headers=Headers, 
        json={ 
            "roomId" : class2022, 
            "text" : "This is a test message from API using Python script"
            })

print(response.json())