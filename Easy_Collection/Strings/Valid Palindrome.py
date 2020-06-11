class Solution:
    def isPalindrome(self, s: str) -> bool:
            alnum = filter(lambda x:x.isalnum(), s)
            lower = list(map(lambda a: a.lower(), alnum))
            return lower==lower[::-1]
