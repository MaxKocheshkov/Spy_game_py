import requests
from class_vk import GROUP_SUB_URL


class Group:
    def __init__(self, token, group_ids):
        self.token = token
        self.group_ids = group_ids

    def uniq_group(self):
        find_groups = requests.get(
            GROUP_SUB_URL,
            params={
                'access_token': self.token,
                'group_ids': self.group_ids,
                'fields': 'members_count',
                'v': 5.103,
            },
        )
        return find_groups.json()
