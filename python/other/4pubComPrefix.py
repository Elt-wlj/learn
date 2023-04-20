# public Front


class Solution:
    def pubcom(self, strs):
        pre = ''
        if not strs:
            return pre
        lens = [len(s) for s in strs]
        m_len = min(lens)
        print('m_len',type(m_len))
        for i in range(m_len):
            c = strs[0][i]
            print('c',c)
            f = True
            for s in strs[1::]:
                print('s',s)
                if s[i] != c:
                    f = False
                    break
            if f:
                pre = pre + c
            else:
                break
        return ('value: ', pre)


strs = ['qwer', 'qasdf', 'qzxcv', 'qazxcv']
s = Solution()
print(s.pubcom(strs))
