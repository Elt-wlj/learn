# luoma number
# I V X L C D M
def roma(s):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
        print('i',i)
        if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
            # ans -= a[s[i]]
            ans = ans - a[s[i]]
            # print('这个是：',s[i])
            # print('后面这个是：', s[i+1])
        else:
            # ans += a[s[i]]
            ans = ans + a[s[i]]
            # print('else这个是：', s[i])
    return ans


print(roma('VX'))
