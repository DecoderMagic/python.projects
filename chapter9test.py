dict1 = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
dict2 = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
dict3 = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}

course_number = input('Enter course number here: ')

if course_number in dict1:
    print('Room number: ', dict1[course_number])
    print('Instructor name: ', dict2[course_number])
    print('Meeting time: ', dict3[course_number])
else:
    print('Course not found!')
    print('Please try again.')
