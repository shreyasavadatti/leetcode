class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lstrip()
        i=0
        sign=1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        else:
            pass
        c=0
        while i<len(s):
            if not (s[i]).isdigit():
                break
            else:
                c=c*10+int(s[i])
                i=i+1
        c=c*sign
        if c<=-2**31:
            return -2**31
        elif c>2**31-1:
            return 2**31-1
        else:
            return c
        