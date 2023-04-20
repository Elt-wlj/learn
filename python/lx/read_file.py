# with open('1.txt',encoding='utf-8') as file_name:
#     conta = file_name.read()
#     print(conta)
# file_name.close()

# file_path='1.txt'
# with open(file_path) as file_name:
#     for line in file_name:
#         print(line.rstrip())
    
file_path = '1.txt'
with open(file_path,'a') as file_name:
    file_name.write('hahahahhah')
file_name.close()