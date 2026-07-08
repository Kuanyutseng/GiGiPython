student_profile = {
    'name': 'Gigi',
    'courses': ['Math', 'English', 'Physics', 'Chemistry'],
    'certs': {'TOEIC', 'TQC'},
    'scores': {'Math': 88, 'English': 94, 'Physics': 72}
}
student_profile['courses'].insert(1, 'Biology')
student_profile['courses'].remove('Chemistry')
student_profile['certs'].add('AWS')
if 'TOEIC' in student_profile['certs']:
    student_profile['scores']['English'] += 5
    if student_profile['scores']['English'] > 100:
        student_profile['scores']['English'] = 100
    else:
        print (tuple(student_profile['courses'][1:3]))

if 'Physics' in student_profile['scores'] and student_profile['scores']['Physics'] < 75:
    if 'Chemistry' in student_profile['courses']:
        print('需重修物理與化學')
    if 'Chemistry' not in student_profile['courses'] and student_profile['scores']['Math'] > 85:
        student_profile['scores']['Physics'] += 3
        print("物理成績偏低，但數學表現良好，已安排物理輔導課程。")
    else:
        print("學業狀態待加強，需重修物理。")
else:
    print("學業狀態良好。")
    
print(sorted(student_profile['scores']))
print(student_profile)