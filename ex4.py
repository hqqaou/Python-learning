# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:23:36 2019

@author: 贺琦琦
"""

print('Let us start for variables and names!')
cars=100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven

print('There are %d cars available',cars)
print('There are only %d drivers available',drivers)
print('There will be %d empty cars today',cars_not_driven)
print('We can transport %d people today', carpool_capacity )
print('We have %d to carpool today',passengers)
print("We need to put about", average_passengers_per_car, "in each car.")