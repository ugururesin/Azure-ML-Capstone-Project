import json
import requests

# URL for the web service, should be similar to:
scoring_uri = 'http://5544066d-8189-4314-b211-340ae34e758b.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '2BEdNHFWFFx6Df01RlQFW6l2Su8I6Wvm'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
           "age": 50, 
           "anaemia": 0, 
           "creatinine_phosphokinase": 250, 
           "diabetes": 0, 
           "ejection_fraction": 15, 
           "high_blood_pressure": 1, 
           "platelets": 250000, 
           "serum_creatinine": 1.5, 
           "serum_sodium": 100, 
           "sex": 0, 
           "smoking": 0,
           "time": 3
          },
          {
           "age": 30, 
           "anaemia": 0, 
           "creatinine_phosphokinase": 2000, 
           "diabetes": 1, 
           "ejection_fraction": 30, 
           "high_blood_pressure": 1, 
           "platelets": 280000, 
           "serum_creatinine": 0.5, 
           "serum_sodium": 150, 
           "sex": 1, 
           "smoking": 0,
           "time": 40
          },
      ]
    }
# converting to the data to JSON
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# setting the content type
headers = {'Content-Type': 'application/json'}
# if the authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# printing the prediction
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
