class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = dict() #map from array of character-wise frequencies --> list of anagrams 

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char)-ord("a")] += 1

            key = tuple(arr)

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        
        return list(d.values())

            
