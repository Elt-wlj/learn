import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# input_values = ['T','E','S','T','N','O']
# s = [1,4,9,23,30,100]
# plt.plot(input_values,s,linewidth = 5)
# plt.title('TEST',fontsize = 12)
# plt.xlabel('key',fontsize = 12)
# plt.ylabel('value',fontsize = 12)
# plt.tick_params(axis='both',labelsize=14)
# plt.show()
font_set = FontProperties(fname=r'c:\windows\fonts\FZYTK.TTF',size=15)
x_num = ['录入', '办公自动化', 'C语言', '计算机', 'CDR']
y_num2 = ['AQQ', 'BQQ', 'CQQ', 'DQQ', 'EQQ']
plt.plot(x_num,label='测试',marker = '*')
plt.legend(prop={'family': 'SimHei', 'size': 15})
plt.scatter(x_num, y_num2, edgecolors='none', c=(0, 0.3, 0.5), cmap=plt.cm.Greens,)
plt.title('test')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.savefig('1.png', bbox_inches='tight')
plt.show()
