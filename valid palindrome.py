import re
def isPalindrome(s):
        s = s.lower()
        #removes anything that is not a alphabet or number
        s = re.sub('[^a-z0-9]','',s)
        #checks for palindrome
        if s == s[::-1]: 
            return True
        else:
            return False
        
        
s = str(input("Enter the string: "))
print(isPalindrome(s))