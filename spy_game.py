from urllib.parse import urlencode
import requests
from pprint import pprint
import time 
from requests.exceptions import Timeout

user_id = input('Введите id пользователя 1: ')

APP_ID = 7416043
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'user',
    'response_type': 'token',
    'v': '5.52'
}
"""
#Получение ссылки с токеном

print('?'.join(
    (OAUTH_URL, urlencode(OAUTH_PARAMS))
))
"""
TOKEN = 'b95fc08473c55936c3187c071f5a668c51f7d03868bd896a0cafcd9ea41e63b0c4614c4c334aa9f55bcc8'

class USER():
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id 

    def get_user(self):
        user_info = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token,
                'user_ids': self.user_id,
                'v': 5.103, 
            }
        )
        return user_info.json()

    def get_groups(self):
        user_groups = requests.get(
            'https://api.vk.com/method/groups.get',
            params={
                'access_token': self.token,
                'user_id': self.user_id,
                'extended': 1,
                'v': 5.103, 
            },
        )
        return user_groups.json()

    def get_friends(self):
        user_friends = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'user_id': self.user_id,
                'v': 5.103, 
                }
        )
        return user_friends.json()

# class Group():
#     def __init__(self, token, group_id):
#         self.token = token
#         self.group_id = group_id 

#     def groups_item(self):
#         group = requests.get(
#             'https://api.vk.com/method/groups.getMembers',
#             params={
#                 'access_token': self.token,
#                 'group_id': self.group_id,
#                 'v': 5.103, 
#                 }
#         )
#         return group.json()
    
#     def res_group(self):
#         resalt = requests.get(
#             'https://api.vk.com/method/groups.getById',
#             params={
#                 'access_token': self.token,
#                 'group_id': self.group_id,
#                 'v': 5.103, 
#                 }
#         )
#         return resalt.json()


def output():
    user1 = USER(TOKEN, user_id)
    for friends in user1.get_friends().values():
        user_fr = friends.get('items')       
        for i in range(0, len(user_fr)):
            code = "var user_fr;\
                    var groups = [];\
                    var i; while(i <= user_fr.lenght){groups.push(API.groups.get({'user_id': user_fr[i], 'extended' : 1}));} return groups;"
            time.sleep(0.5) 
            try:
                resalt = requests.get('https://api.vk.com/method/execute', params={'user_id': user_id, 'access_token': TOKEN, 'v': 5.103, 'code': code}, timeout = 720)
            except Timeout:
                print('The request timed out')
            else:
                print(resalt.status_code)
                return resalt.json()
    
pprint(output())




