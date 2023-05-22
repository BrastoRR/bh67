def dict_of_dict(mydict):
    mistakes = list()
    for key, value in mydict.items():
        if not mydict[key].get('email'):
            mistakes.append(mydict[key]['name'])
    return mistakes


print(dict_of_dict(
    mydict={
              'id_120190': {'name': 'Ivan', 'last_name': '', 'phone': '555-66-77', 'email': 'ivaiva@tut.by'},
              'id_199203': {'name': 'Petya', 'last_name': 'Ivushkin', 'phone': '555-23-43', 'email': 'iva@mail.ru'},
              'id_130213': {'name': 'Artur', 'last_name': 'Valuev', 'phone': '555-66-66', '': 'valuev@mail.ru'},
              'id_120343': {'name': 'Oleg', 'last_name': 'Petrikov', '': '', 'email': 'oleole@gmail.com'},
              'id_110876': {'name': 'Pavel', 'last_name': 'Pavlov', 'phone': '555-12-23', 'email': ''}
    }
))
