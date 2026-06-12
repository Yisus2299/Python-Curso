student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

#Looping through dictiones:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

Student_data_frame = pandas.DataFrame(student_dict)
# print(Student_data_frame)#: dara este resultado:
'''  student  score
0  Angela     56
1   James     76
2    Lily     98 
'''

#loop through a dara frame
for (key, value) in Student_data_frame.items():
#   print(value): dara como resultado:
    '''0    Angela
1     James
2      Lily
Name: student, dtype: str
0    56
1    76
2    98'''

for (index, row) in Student_data_frame.iterrows():
    # print(row.student) #el student es de la lista: "student": ["Angela", "James", "Lily"]
    if row.student == "Angela":
        # print(row.score) : "score": [56, 76, 98]
        print(row.score)