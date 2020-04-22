from urllib.parse import urlencode
import requests
from pprint import pprint

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