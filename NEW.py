class Solution(object):
    def isPalindrome(self, x):
        digit = 0 
        while True:
            if x < 0 :
                return False
            elif x >= 0:
                backup = x
                while x > 0:
                    mod = x % 10
                    adigit =  digit * 10
                    digit = mod + adigit          
                    x = x // 10
                if digit == backup :
                    return True
                else :
                    return False


print("Yoo newv2")