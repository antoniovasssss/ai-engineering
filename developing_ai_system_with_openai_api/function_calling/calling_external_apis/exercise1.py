""" 
Calling APIs in Python (requests Library)
"""
import requests

url="https://api.artic.edu/api/v1/artworks/search" # API Endpoint

params= {
"q":"seaside"
} # Params: input values for API

response=requests.request("GET",url,params=params) # GET: type of request

data=response.json() # converts the response to a Python dictionary

print(data)