import json
import requests

headers = {'Accept': 'application/json'}

def api_test(url):
    response = None
    api = None
    # detect sigup or signin
    if ("signup" in url):
        input_signup = {"email":"ntc-test-123@gmail.com", "username":"1111111111", "password":"1111111111"}
        api = "signup"
        response = requests.post('https://beta-eid-backend.townway.com.tw/accounts/signup', data = input_signup, headers=headers)
    elif ("signin" in url):
        input_signin = {"email":"ntc-test-123@gmail.com", "password":"1111111111"}
        api = "signin"
        response = requests.post('https://beta-eid-backend.townway.com.tw/accounts/signin', data = input_signin, headers=headers)

    return api, response.text
