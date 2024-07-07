immutable_var = 1, 2, 'summer', 'cherry', True
print(immutable_var)
#immutable_var[3] = 'spring' - изменить значение элемента кортежа ('cherry')  нельзя, потому что оно неизменяемое, т.к. кортеж не поддерживает обращение по элементам
mutable_list = [3, 4, 'apple', 'phone']
print(mutable_list)
mutable_list[3] = 'pineapple'
print(mutable_list)
