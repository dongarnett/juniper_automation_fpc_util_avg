#!/usr/bin/env python3


def determine_list_highest_value(list_name):
    list_max = max(list_name)
    return list_max

def determine_list_average(list_name):
    new_list = list_name
    element_cnt = len(new_list)
    sum_of_numbers = float(sum(new_list))
    avg = sum_of_numbers / element_cnt
    return avg
