class Solution:
    def convertToTitle(self, n: int) -> str:
        # 递归处理
        if (n-1)//26 == 0:
            return chr( 65 + (n-1) % 26 )
        else:
            return self.convertToTitle( (n-1)//26 ) + chr(65 + (n-1) % 26)
