class Solution:
    def reverse(self, x: int) -> int:
        
        #判斷正負數
        if x > 0:
            negativeSign = 1
        elif x == 0:
            return 0
        else:
            negativeSign = -1
            
        inputNumber = abs(x) 
        outputNumber = 0
        
        while inputNumber != 0:
            #商數
            quotion = inputNumber // 10
            #餘數
            remainder = inputNumber % 10 
            
            inputNumber = quotion
            outputNumber = outputNumber*10 + remainder

        if outputNumber > 2**31:
            return 0

        return outputNumber * negativeSign
