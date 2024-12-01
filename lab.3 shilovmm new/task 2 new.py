# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, divider=','):
    common_members = list(set(first.split(divider)).intersection(second.split(divider)))

    common_members.sort()
    return common_members


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
