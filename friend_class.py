from class_vk import Vk, TOKEN, user_id, params
from user_class import User
import time
from tqdm import tqdm
import sys


class Friends(Vk):

    def get_friends_group(self):
        user1 = User(TOKEN, user_id)
        friends_group_set = set()
        for user_friends in user1.get_friends().values():
            friends_id_list = user_friends.get('items')
            friends_group_list = []
            for friend_id in friends_id_list:
                fr_param = {'user_id': friend_id}
                params.update(fr_param)
                friend = User(TOKEN, friend_id)
                for friend_gr in friend.get_groups().values():
                    fr_groups = friend_gr.get('items')
                    time.sleep(0.5)
                    if fr_groups is not None:
                        for fr_gr in tqdm(fr_groups, file=sys.__stdout__):
                            time.sleep(0.1)
                            friends_group_list.append(fr_gr.get('id'))
                            friends_group_set = set(friends_group_list)
        return friends_group_set
