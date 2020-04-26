from urllib.parse import urlencode
import requests
import time

# APP_ID = 7416043
# OAUTH_URL = 'https://oauth.vk.com/authorize'
# OAUTH_PARAMS = {
#     'client_id': APP_ID,
#     'display': 'page',
#     'scope': 'user',
#     'response_type': 'token',
#     'v': '5.52'
# }
"""
#Получение ссылки с токеном

print('?'.join(
    (OAUTH_URL, urlencode(OAUTH_PARAMS))
))
"""
user_id = input('Введите id пользователя: ')

# TOKEN = 'e0d324ac344b394d5bbceac58094941615a4de4604b6145f390290e35efb04e0b9e8f0f281a2292c55902'
TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

params = {
    'access_token': TOKEN,
    'user_ids': user_id,
    'v': 5.103,
}

url_us = 'https://api.vk.com/method/users.get'
url_fr = 'https://api.vk.com/method/friends.get'
url_gr = 'https://api.vk.com/method/groups.get'
url_gr_bi = 'https://api.vk.com/method/groups.getById'


class Vk:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_request(self, url, params):
        request = requests.get(
            url,
            params,
        )
        return request.json()

    def log(self, url):
        request = requests.get(url)
        process_time = round(time.perf_counter())
        while request.status_code == 200:
            return f'execution status = {request.status_code} \b Search data load time: {process_time}'
