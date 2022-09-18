import utlis
import re
from typing import Any

def check_fitness(dict_student: dict,dict_profession: dict) -> dict:
    '''
    Проводит проверку пригодности студента, сравнивая скилы из словарей
    :param student: номер студента из файла student.json
    :param profession: профессия из файла profession.json
    :return: итоговый словарь с данными для вывода
    '''
    student_skills: set = set(list(dict_student['skills']))
    profession_skills: set = set(list(dict_profession['skills']))
    final_dict: dict[str, Any[list, int]] = {}
    final_dict['has'] = list(student_skills.intersection(profession_skills))
    final_dict['lacks'] = list(profession_skills.difference(student_skills))
    final_dict['fit_percent'] = int((len(list(student_skills.intersection(profession_skills))) * 100 / (
        len(list(dict_profession['skills'])))))
    return final_dict


def check_login(nickname: str) -> bool:
    '''
    Проверяет логин клиента
    :param nickname: Ник клиента из файла student.json
    :return: возвращает верно ли заполнен ник
    '''
    pattern = r'(?=.*[\W])(?=.*[\d])(?=.*[A-Z])(?=^[^A-Z])(?=.*[\w]$).{4,}'
    if bool(re.search(pattern, nickname)) == True:
        return True
    else:
        return False



def main():
    '''
    Основная функция
    '''
    try:
        user_input: int = int(input(f'Программа: Введите номер студента\nПользователь: '))
        dict_student: dict = utlis.get_student_by_pk(user_input)
        nickname: str = dict_student['login']
        if check_login(nickname) == False:
            print('incorrect login')
            quit()
        if dict_student == False:
            print('Программа: У Вас нет такого студента')
            quit()
        else:
            student_name: str = dict_student['full_name']
            student_skills: str = ', '.join(dict_student['skills'])
            print(f'Программа: Студент {student_name}\nПрограмма: Знает: {student_skills}')
        user_input2: str = input(f'Программа: Выберите специальность для оценки студента {student_name} - ').title()
        dict_profession: dict = utlis.get_profession_by_title(user_input2)
        if user_input2 == False:
            print('Программа: У Вас нет такой специальности')
            quit()
        else:
            final_dict: dict = check_fitness(dict_student, dict_profession)
            has: str = ', '.join(final_dict['has'])
            lacks: str = ', '.join(final_dict['lacks'])
            print(f'Программа: Пригодность {final_dict["fit_percent"]}%')
            print(f'Программа: {student_name} знает {has}' if len(has) != 0
                  else f'Программа: {student_name} не знает нужных языков')
            print(f'Программа: {student_name} не знает {lacks}' if len(lacks) != 0
                  else f'Программа: {student_name} знает все требуемые языки')
    except:
        print('incorrect input')






main()


