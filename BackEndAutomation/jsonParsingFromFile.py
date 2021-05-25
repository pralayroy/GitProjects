import json

with open('D:\\Learnings\\Python\PyCharm\\PycharmProjects\\courses.json') as dict:
    data = json.load(dict)
    # print(data)
    print(type(data))
    # list_of_courses = data['courses'][1]['title']
    # print(list_of_courses)
    dashboard_list = data['dashboard']['website']
    # print(dashboard_list)

    # Get the price of course RPA
    list_of_courses = data['courses']
    print(type(list_of_courses))
    print(list_of_courses)
    for course in list_of_courses:
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45

# compair two json file
with open('D:\\Learnings\\Python\PyCharm\\PycharmProjects\\courses1.json') as dict1:
    data1 = json.load(dict1)
    print(data == data1)
    assert data == data1
