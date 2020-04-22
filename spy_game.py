from urllib.parse import urlencode
import requests
from pprint import pprint
import time 
from init import USER
import datetime
import logging
from contextlib import contextmanager

user_id = input('Введите id пользователя: ')

start_time = datetime.datetime.utcnow()

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
TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

@contextmanager
def logger():
  try:
    logger = logging.getLogger("find groups")
    logger.setLevel(logging.INFO)
    fh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("Program started")
    yield
    end_time = datetime.datetime.utcnow()
    print('Время работы: {}'.format(end_time - start_time))
  finally:
    logger.info("Done!")

main = logger()

with main:
    user1 = USER(TOKEN, user_id)
    user_group_list = []
    for user_gr in user1.get_groups().values():
        us_groups = user_gr.get('items')
        time.sleep(0.5)
        for us_gr in us_groups:
            user_group_list.append(us_gr.get('id'))
        user_group_set = set(user_group_list)

    for user_friends in user1.get_friends().values():
        friends_id_list = user_friends.get('items')
    friends_group_list =[]
    for friend_id in friends_id_list:
        friend = USER(TOKEN, friend_id)
        for friend_gr in friend.get_groups().values():
            fr_groups = friend_gr.get('items')
            time.sleep(0.5)
            if fr_groups != None:
                for fr_gr in fr_groups:
                    friends_group_list.append(fr_gr.get('id'))
                    friends_group_set = set(friends_group_list)
    difference_list = user_group_set.difference(friends_group_set)

    print(f'Список групп пользователя {user_id}: {user_group_set}')
    # print(f'А вот список групп которые мы искали - {list(difference_list)}')
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
                        # 'fields': self.members_count,
                        'v': 5.103, 
                    },
                )
            return find_groups.json()
            
    print(f'Группы на которые подписан только пользователь {user_id}: \n')
    for i in list(difference_list):
        output_gr = GROUP(TOKEN, i)
        pprint(output_gr.uniq_group())