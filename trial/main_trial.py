# -*- coding: UTF-8 -*-
import pkg_naming.naming_machine as nm
for idx in range(10):
    new_name = nm.pick_a_full_name()
    print(new_name)

print("-----------------boy----------------")
for idx in range(10):
    new_name = nm.pick_a_full_name_by_sex(1)
    print(new_name)

print("-----------------girl----------------")
for idx in range(15):
    new_name = nm.pick_a_full_name_by_sex(2)
    print(new_name)
