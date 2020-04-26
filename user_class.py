from urllib.parse import urlencode
import requests
from vk_class import Vk, TOKEN, user_id, params, url_fr, url_gr, url_us
import time


class User(Vk):

    # def get_user(self):
    #     user_info = requests.get(
    #         url_us,
    #         params,
    #     )
    #     return user_info.json()

    def get_groups(self):
        user_groups = requests.get(
            url_gr,
            params,
        )
        return user_groups.json()

    def get_friends(self):
        user_friends = requests.get(
            url_fr,
            params,
        )
        return user_friends.json()  # независимо от вводимого id пользовователя выдает одинаковый набор id людей на которых не подписан пользователь

    def get_user_groups(self):
        for user_gr in User(TOKEN, user_id).get_groups().values():
            us_groups = user_gr.get('items')
            time.sleep(0.5)
            user_group_set = set(us_groups)
        return user_group_set  # независимо от вводимого id пользовователя выдает одинаковый набор id групп на которые не подписан пользователь
