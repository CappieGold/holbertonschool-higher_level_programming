#!/usr/bin/python3
def no_c(my_string):
    liste = list(my_string)
    delete_c = "c"
    delete_C = "C"
    while delete_c in liste:
        liste.remove(delete_c)
    while delete_C in liste:
        liste.remove(delete_C)
    my_string = ''.join(liste)
    return my_string
# new_string = "".join(i for i in my_string if i not in 'cC')
