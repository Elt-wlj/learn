class AddOne:
    def AddOneNumber(self, number: list):
        s = ''
        l = []
        for i in number:
            s = s + str(i)
        for n in str(int(s) +1):
            l.append(int(n))
        return l



number = [5,9,7]
add_one = AddOne()
print(add_one.AddOneNumber(number))
