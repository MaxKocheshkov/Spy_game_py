import requests


user_id = input('Введите id пользователя: ')

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

USER_URL = 'http://api.vk.com/method/users.get'
FRIEND_URL = 'http://api.vk.com/method/friends.get'
GROUP_URL = 'http://api.vk.com/method/groups.get'
GROUP_SUB_URL = 'http://api.vk.com/method/groups.getById'

params = {
    'access_token': TOKEN,
    'user_id': user_id,
    'v': 5.103,
}


class Vk:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_request(self, url, params):
        response = requests.get(
            url,
            params,
        )
        return response.json()

