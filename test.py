import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

def test_all():
    # 1. Register
    print("1. Registering user...")
    response = requests.post(f"{BASE_URL}/users/register/", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
        "bio": "Test user"
    })
    print(f"Registration: {response.status_code}")
    
    # 2. Login
    print("\n2. Logging in...")
    response = requests.post(f"{BASE_URL}/users/token/", json={
        "username": "testuser",
        "password": "password123"
    })
    token = response.json()["access"]
    print(f"Login: {response.status_code}")
    
    # 3. Create post
    print("\n3. Creating post...")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/posts/", 
        headers=headers,
        json={"content": "Test post from script"}
    )
    print(f"Create post: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # 4. List posts
    print("\n4. Listing posts...")
    response = requests.get(f"{BASE_URL}/posts/", headers=headers)
    print(f"List posts: {response.status_code}")
    print(f"Posts: {response.json()}")

if __name__ == "__main__":
    test_all()