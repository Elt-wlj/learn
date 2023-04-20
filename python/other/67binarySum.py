class BinarySum:
    def Binary_sum(self,a,b):
        print(int(a,2))
        print(int(b,2))
        return bin(int(a,2)+int(b,2))[2:]

a = "11"
b = "1"
bs = BinarySum()
print(bs.Binary_sum(a,b))