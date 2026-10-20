class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^\w\s]', '', s.lower())
        result = "".join(result.split())
        return result == result[::-1]

        
        