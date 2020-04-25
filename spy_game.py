from pprint import pprint
from vk_class import TOKEN, user_id, Vk
from user_class import User
from group_class import Group


def difference_groups():
    difference_list = User(TOKEN, user_id).get_user_groups().difference(Group(TOKEN, user_id).get_friends_group())
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
    pprint(difference_groups())
