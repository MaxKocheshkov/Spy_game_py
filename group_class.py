from urllib.parse import urlencode
import requests
from vk_class import Vk, TOKEN, params, url_gr_bi, user_id, url_fr
from user_class import User
import time


class Group(Vk):

    def uniq_group(self):
        params_uq_gr = {'group_id': self.group_id, 'fields': 'members_count'}
        params.update(params_uq_gr)
        find_groups = requests.get(
            url_gr_bi,
            params,
        )
        return find_groups.json()

    def get_friends_group(self):
        for user_friends in User(TOKEN, user_id).get_friends().values():
            friends_id_list = user_friends.get('items')
        for friend_id in friends_id_list:
            friend = User(TOKEN, friend_id)
            for friend_gr in friend.get_groups().values():
                fr_groups = friend_gr.get('items')
                time.sleep(0.5)
                if fr_groups != None:
                    friends_group_set = set(fr_groups)
        return friends_group_set  # независимо от вводимого id пользовователя выдает одинаковый набор id групп аналогичный выдаваемому в методе get_user_groups
