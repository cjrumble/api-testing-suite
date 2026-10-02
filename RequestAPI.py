"""REST API CRUD smoke test example.

The API credential is supplied through GOREST_API_TOKEN and is never stored
in source control.
"""
import os, random, string, requests
BASE_URL = "https://gorest.co.in"
AUTH_TOKEN = os.getenv("GOREST_API_TOKEN")
if not AUTH_TOKEN:
    raise RuntimeError("GOREST_API_TOKEN is not set; never hard-code API credentials.")
HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}"}

def generate_random_email():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10)) + "@automation.com"

def get_request():
    response = requests.get(f"{BASE_URL}/public/v2/users", headers=HEADERS, timeout=30)
    assert response.status_code == 200
    return response.json()

def post_request():
    data = {"name":"API Automation Test","email":generate_random_email(),"gender":"male","status":"active"}
    response = requests.post(f"{BASE_URL}/public/v2/users", json=data, headers=HEADERS, timeout=30)
    assert response.status_code == 201
    body=response.json(); assert body["name"] == data["name"]; return body["id"]

def put_request(user_id):
    data={"name":"API Automation Updated","email":generate_random_email(),"gender":"male","status":"inactive"}
    response=requests.put(f"{BASE_URL}/public/v2/users/{user_id}",json=data,headers=HEADERS,timeout=30)
    assert response.status_code == 200; assert response.json()["id"] == user_id

def delete_request(user_id):
    response=requests.delete(f"{BASE_URL}/public/v2/users/{user_id}",headers=HEADERS,timeout=30)
    assert response.status_code == 204

if __name__ == "__main__":
    get_request(); user_id=post_request(); put_request(user_id); delete_request(user_id)
