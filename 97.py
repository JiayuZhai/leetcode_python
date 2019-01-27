class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        re = dict()
    
        def f(str1, str2, str3):
            if len(str2) == 0:
                if str1 == str3:
                    re[(str1, str2, str3)] = True
                else:
                    re[(str1, str2, str3)] = False
            if len(str1) == 0:
                if str2 == str3:
                    re[(str1, str2, str3)] = True
                else:
                    re[(str1, str2, str3)] = False
            if (str1, str2, str3) not in re.keys() and (str2, str1, str3) not in re.keys():
                if str3[0] != str1[0] and str3[0] != str2[0]:
                    re[(str1, str2, str3)] = False
                elif str3[0] == str1[0] and str3[0] == str2[0]:
                    re[(str1, str2, str3)] = f(str1[1:], str2, str3[1:]) or f(str1, str2[1:], str3[1:])
                elif str3[0] == str1[0]:
                    re[(str1, str2, str3)] = f(str1[1:], str2, str3[1:]) 
                elif str3[0] == str2[0]:
                    re[(str1, str2, str3)] = f(str1, str2[1:], str3[1:])

            if (str1, str2, str3) in re.keys():
                return re[(str1, str2, str3)]
            else:
                return re[(str2, str1, str3)]

        if len(s1) + len(s2) != len(s3):
            return False
        return f(s1, s2, s3)
