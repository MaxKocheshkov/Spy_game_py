from pprint import pprint
from user_class import User
from group_class import Group
from friend_class import Friends
from class_vk import TOKEN, user_id
import json


def difference_groups():
    difference_list = (User(TOKEN, user_id).get_user_groups()).difference(Friends(TOKEN, user_id).get_friends_group())
    final_group_list = []
    for i in list(difference_list):
        output_gr = Group(TOKEN, i)
        for value in output_gr.uniq_group().values():
            for groups_dict in value:
                final_group_dict = {'name': groups_dict['name'], 'gid': groups_dict['id'],
                                    'members_count': groups_dict['members_count']}
                final_group_list.append(final_group_dict)
    return final_group_list


if __name__ == '__main__':
    print(f'Список групп пользователя {user_id}: {User(TOKEN, user_id).get_user_groups()}')
    print(f'Группы на которые подписан только пользователь {user_id}:')
    with open('groups.json', "w") as file:
        json.dump(difference_groups(), file, sort_keys=True, indent=2)
    with open('groups.json', 'r') as open_file:
        group_dict = json.load(open_file)
        pprint(group_dict)
