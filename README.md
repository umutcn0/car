# Car App

### Setup
- $sudo docker compose down --remove-orphans && sudo docker compose up --build

- The project default port has been assigned as **0.0.0.0:8001** inside the Docker compose and the settings of the project.


## Endpoint Explanations

-  **/api/docs** -> Swagger documentation 
-  **/api/auth/token?{username}** -> Generates Token. (GET)
-  **/api/car/car-info?{car_id}** -> Get car info by its' id. (GET)
-  **/api/car/update** -> Update car information. (POST)
-  **/api/car/delete?{car_id}** -> Delete car by its' id. (DELETE)
-  **/api/car/list** -> List cars by giving parameters. (GET)
-  **/api/car/upload** -> Upload data to the database. (POST)
-  **/api/car/add** -> Add new car to the database. (POST)

## Get Token

- Send a **GET** request to **http://0.0.0.0:8001/api/auth/token/{username}** address.


## Python Endpoint Request Examples

- Python snippet for sending requests via *requests* library.
```
import requests
import json

token_response = requests.post("http://0.0.0.0:8001/api/auth/token?username='umut'")
token = token_response.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

response = requests.get("http://0.0.0.0:8001/api-endpoints/")
for key, value in response.json().items():
    print(json.dumps(value, indent=4))

```

## Example Data Types For Filtering, Updating and Listing

- This section related to POST and GET endpoints that,  
1. http://0.0.0.0:8001/api/car/update (POST)
2. http://0.0.0.0:8001/api/car/list (GET)
**You can use same parameters with these functions.**

**PARAMETERS:**
- make
- model
- trim
- body
- transmission
- state
- condition
- odometer
- color
- interior
- price

### List Endpoint
- Filtering particular table with limiting option. Pass the filter from the url. You must pass all parameters from the url. The function request type is GET.

#### Additional parameters for this function are:
- page
- size
- year

### Update Endpoint
- This function will update the existing Car. You must pass a car_id to update an entity.You must pass all parameters as JSON. The function request type is POST.

#### Additional parameters for this function are:
- car_id

```
filter_data = {
        "car_id":1,
        "make": "Hyundai",
        "price": 1000000,
        "odometer": 200000
        }
```
