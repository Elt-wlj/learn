# while True:
#     fir_num = input('first number: ')
#     if fir_num == 'q':
#         break
#     sec_num = input('second_num: ')
#     if sec_num == 'q':
#         break
#     try:
#         answer = int(fir_num) / int(sec_num)
#     except ZeroDivisionError:
#         print('您输入的不对')
#     else:
#         print(answer)
# file_path = '123.txt'
# try:
#     with open(file_path) as file_name:
#         con = file_name.read()
# except FileNotFoundError:
#     print('该文件不存在')

# import json
# num = [2,3,4,5,10,28]
# file_name = '1.json'
# with open(file_name,'w') as file_obj:
#     json.dump(num,file_obj)
# file_obj.close()
# import json
# username = input('what are u doing')
# file_path = '1.json'
# with open(file_path,'w') as f:
#     json.dump(username,f)
#     print('doing '+ username +'!')
# f.close()

import json


def get_sored_test():
    filename = '2.json'
    try:
        with open(filename) as f:
            test = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return test

def greet_user():
    test1 = get_sored_test()
    if test1:
        print('ceshi' + test1)
    else:
        test = input('what ???test:')
        file_path = '1.json'
        with open(file_path,'w') as f:
            json.dump(test,f)
            print('welcome '+ test )
greet_user()

