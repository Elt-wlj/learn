import re
class LastWordlenth:
    def read_word(self,str):
        return len(str.strip().split()[-1])

str = "   fly me   to   the moon  "
lw = LastWordlenth()
print(lw.read_word(str))