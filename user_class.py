from urllib.parse import urlencode
import requests
from pprint import pprint

API = 'https://api.vk.com/method'

params = {
        'access_token': self.token,
        'user_ids': self.user_id,
        'v': 5.103, 
}

class USER():
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id 

    def get_user(self):
        user_info = requests.get(
            'API/users.get',
            params = params
        )
        return user_info.json()

    def get_groups(self):
        user_groups = requests.get(
            'API/groups.get',
            params = params
        )
        return user_groups.json()

    def get_friends(self):
        user_friends = requests.get(
            'API/friends.get',
            params = params
        )
        return user_friends.json()

    