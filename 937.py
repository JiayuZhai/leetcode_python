class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dig = []
        letter = {}
        for log in logs:
            if ord(log.split()[1][0]) in range(48, 58):
                dig.append(log)
            else:
                letter[log.split(' ', 1)[1]] = log.split(' ', 1)[0]
        result = []
        for key in sorted(letter.keys()):
            s = letter[key] + ' ' + key
            result.append(s)
        result = result + dig
        return result
