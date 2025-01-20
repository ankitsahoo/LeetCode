class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        
        left, right = 0, len(s_list) - 1
        
        while left < right:
            if s_list[left] not in vowels:
                left += 1
                continue
            if s_list[right] not in vowels:
                right -= 1
                continue
            s
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            left += 1
            right -= 1
        
        return ''.join(s_list)  # Convert list back to string