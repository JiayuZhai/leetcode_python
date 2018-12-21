class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num == 0):
            return "Zero"
        result = "";
        if (num > 999999999):
            result += self.numberToWordsWithThreeDIgit(num // 1000000000) + " Billion"
            num %= 1000000000
 
        if (num > 999999):
            result += self.numberToWordsWithThreeDIgit(num // 1000000) + " Million"
            num %= 1000000
 
        if (num > 999):
            result += self.numberToWordsWithThreeDIgit(num // 1000) + " Thousand"
            num %= 1000
 
        if (num > 0):
            result += self.numberToWordsWithThreeDIgit(num)
 
        return result.strip()
 
    def numberToWordsWithThreeDIgit(self, num):
        num1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        num2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        result = ""
        if (num > 99):
            result += " " + num1[num // 100 - 1] + " Hundred"
            num %= 100
        if (num > 19):
            result += " " + tens[num // 10 - 2]
            num %= 10
        if (num > 9):
            result += " " + num2[num - 10]
            num = 0
 
        if (num > 0):
            result += " " + num1[num - 1]
 
        return result
 
