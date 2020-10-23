# Дипломный проект «Шпионские игры» курса «Python: программирование на каждый день и сверхбыстрое прототипирование»

## Описание
Выводится список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.

## Входные данные
id пользователя в ВК, для которого мы проводим исследование.

## Выходные данные
Файл groups.json в формате:
'
[
    { 
    “name”: “Название группы”, 
    “gid”: “идентификатор группы”, 
    “members_count”: количество_участников_сообщества
    },
    {
    …
    }
]
'