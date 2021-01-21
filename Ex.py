import json
import requests

site = "https://api.npoint.io/2b57052af2060e84dc86"

# Your code goes here


# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']

# Debug
for _i in text:
    print("parse " + str(_i))


# call the function convert_number
# convert all elements (except the first one) into number and return it as a list
def convert_number(my_list):
    new_list = []
    for i in range(1, len(my_list)):
        new_list.append(int(my_list[i]))
    return new_list


y = convert_number(text[0])
print("y")
print(y)


# call the function replace_number
# replace all number 1 by the number 10 in the function
def replace_number(number_list, being_replace, to_replace):
    for num in number_list:
        if num == being_replace:
            number_list[number_list.index(num)] = to_replace
    return number_list


z = replace_number(number_list=y, being_replace=1, to_replace=10)

print("z")
print(z)

_sum = 0
for i in z:
    _sum = _sum + i
    print("sum = " + str(_sum) + "; i =" + str(i))
print("Total = " + str(_sum))
