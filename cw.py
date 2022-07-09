# f = open ('student.txt',mode = 'w')
# print('file name: ',f.name)
# print('file mode:',f.mode)
# print('file readable: ',f.readable())
# print('file writable :',f.writable())
# print("file closed :",f.close())
# f.close()
# print('file closed:',f.close())

# import os 
# if print(os.path.isfile('student.txt')):
#     f = open ('student.txt')
#     print('file opened')
#     f.close()
# else:
#     print("file not found")
# os.remove('student.txt')
# f1 = open('student.txt',mode = 'r')
# f2 = open ('student1.txt', mode = 'w')
# data = f1.read()
# f2.write(data)
# lst= ['ram\n','shyam\n']
# f.writelines(lst)
# print(f.tell())
# f.seek(2)
# print(f.tell())
# data = f.read()
# print(data)
# for i in data:
#     print(i , end='')
# print(data)
# f1.close()
# f2.close() 
# print('success')

import csv
with open ('abc.csv','w') as f:
    csv_reader = csv.writer(f)
    for i in range(2):
        n = input('enter name')
        a = input('enter address')
        csv_reader.writerow([n,a])
    print('score successful')
