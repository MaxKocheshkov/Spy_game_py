from urllib.parse import urlencode
import requests
from pprint import pprint
 
class GROUP():
    def __init__(self, token, group_ids):
        self.token = token
        self.group_ids = group_ids

    def uniq_group(self):
        find_groups = requests.get(
                'https://api.vk.com/method/groups.getById',
                params={
                    'access_token': self.token,
                    'group_ids': self.group_ids,
                    'fields': 'members_count',
                    'v': 5.103, 
                },
        )
        return find_groups.json()