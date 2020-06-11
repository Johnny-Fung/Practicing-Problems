class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
        # ^ or if needle=="":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if needle in haystack[i:i+len(needle)]:
                return i
        else:
            return -1
        # ^ Try solving without using any built in functions:
        #return haystack.find(needle)
