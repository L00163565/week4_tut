"""
# File : q3.py
# Created : 15-10-2021 10:53
# Author : Snehal Shirsath
# Python Version : 3.9.7
# File Version : v1.0.0
# Description :
"""

import pprint

list_of_courses = ["pyhton", "software engineering", "placements"]

def master_function(option):
    dictionary = {"1" : list_of_LYIT_courses ,"2" : edit_course_name,"3" : data_in_the_list }
    return dictionary.get(option)()


def list_of_LYIT_courses():

    print(list_of_courses)


def edit_course_name():
    index = int(input("enter index to be modify: "))
    list_of_courses[index] = input("enter modified value: ")
    print(list_of_courses)


def data_in_the_list():
    pprint.pprint(list_of_courses)

if __name__ == "__main__":

     while True:
         option =input("choice the number of fuction from 1,2,3: ")
         master_function(option)

