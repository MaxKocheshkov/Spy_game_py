from class_vk import Vk, TOKEN, user_id, params, FRIEND_URL, GROUP_URL
import time
from tqdm import tqdm
import sys


class User(Vk):

    def get_friends(self):
        friends = Vk(TOKEN, user_id).get_request(FRIEND_URL, params)
        return friends

    def get_groups(self):
        group_param = {'extended': 1}
        params.update(group_param)
        user_group = Vk(TOKEN, user_id).get_request(GROUP_URL, params)
        return user_group

    def get_user_groups(self):
        user1 = User(TOKEN, user_id)
        user_group_list = []
        user_group_set = set()
        for user_gr in user1.get_groups().values():
            us_groups = user_gr.get('items')
            time.sleep(0.5)
            if us_groups is not None:
                for us_gr in tqdm(us_groups, file=sys.__stdout__):
                    time.sleep(0.1)
                    user_group_list.append(us_gr.get('id'))
                    user_group_set = set(user_group_list)
        return user_group_set
