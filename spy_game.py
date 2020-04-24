from urllib.parse import urlencode
import requests
from pprint import pprint
import time 
from user_class import USER
from group_class import GROUP

user_id = input('Введите id пользователя: ')

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


def get_user_groups():
    user1 = USER(TOKEN, user_id)    
    user_group_list = []
    for user_gr in user1.get_groups().values():
        us_groups = user_gr.get('items')
        time.sleep(0.5)
        for us_gr in us_groups:
            user_group_list.append(us_gr.get('id'))
            user_group_set = set(user_group_list)
    return user_group_set

def get_friends_group():
    user1 = USER(TOKEN, user_id)
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
        request_fr = requests.get('https://api.vk.com/method/friends.get')
        process_time = round(time.perf_counter())
        print(f'execution status = {request_fr.status_code} \b Friends group search data load time: {process_time}', end='\r')
    return friends_group_set

def difference_groups():
    difference_list = get_user_groups().difference(get_friends_group())
    final_group_list = []
    for i in list(difference_list):
        output_gr = GROUP(TOKEN, i)
        for value in output_gr.uniq_group().values():
            for groups_dict in value:
                final_group_dict = {'name': groups_dict['name'], 'gid': groups_dict['id'], 'members_count': groups_dict['members_count']}
                final_group_list.append(final_group_dict)
            request_gr = requests.get('https://api.vk.com/method/groups.getById')
            process_time = round(time.perf_counter())
            print(f'execution status = {request_gr.status_code} \b Group search data load time: {process_time}', end='\r')
    return final_group_list

if __name__=='__main__':
    print(f'Список групп пользователя {user_id}: {get_user_groups()}')
    print(f'Группы на которые подписан только пользователь {user_id}:')
    pprint(difference_groups())
