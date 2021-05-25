import json

courses = '{ "name" : "Pralay Roy", "language" : ["Python","Java"]}'

# Loads methods parse json string and it returns as dictionary

conv_dict = json.loads(courses)
print(type(conv_dict))
print(conv_dict)
print(conv_dict['name'])
list_language = conv_dict['language']
print(list_language)
print(list_language[0])
