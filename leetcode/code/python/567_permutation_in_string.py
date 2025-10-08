class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        freq_s1, freq_window = [0] * 26, [0] *26
        offset = ord("a")
        for char in s1:
            freq_s1[ord(char) - offset] +=1
        for char in s2[:m]:
            freq_window[ord(char) - offset] += 1
        
        matches = sum(1 for a, b in zip(freq_s1, freq_window) if a == b)
        if matches == 26:
            return True
        
        for right in range(m, n):
            in_idx = ord(s2[right]) - offset
            out_idx = ord(s2[right - m]) - offset

            if freq_window[in_idx] == freq_s1[in_idx]:
                matches -= 1
            freq_window[in_idx] += 1
            if freq_window[in_idx] == freq_s1[in_idx]:
                matches += 1

            if freq_window[out_idx] == freq_s1[out_idx]:
                matches -= 1
            freq_window[out_idx] -= 1
            if freq_window[out_idx] == freq_s1[out_idx]:
                matches += 1
            
            if matches == 26:
                return True
        return False