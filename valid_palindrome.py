class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        array = []
        for i in s.lower():
            if i.isalnum():
                array.append(i)
        return array == array[::-1]