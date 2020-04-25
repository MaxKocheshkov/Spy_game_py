from urllib.parse import urlencode
import requests
from vk_class import Vk, TOKEN, user_id, params, url_fr, url_gr, url_us, url_gr
import time


class User(Vk):

    def get_user(self):
        user_info = requests.get(
            url_us,
            params,
        )
        return user_info.json()

    def get_groups(self):
        params_gr = {'extended': 1, 'fields': 'members_count'}
        params.update(params_gr)
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
        return user_friends.json()

    def get_user_groups(self):
        user_group_list = []
        for user_gr in User(TOKEN, user_id).get_groups().values():
            us_groups = user_gr.get('items')
            time.sleep(0.5)
            for us_gr in us_groups:
                user_group_list.append(us_gr.get('id'))
                user_group_set = set(user_group_list)
            request_gr = requests.get(url_gr)
            process_time = round(time.perf_counter())
            print(f'execution status = {request_gr.status_code} \b User group search data load time: {process_time}',
                  end='\r')
        return user_group_set
