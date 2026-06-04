class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> hm = new HashMap<>();

        for(String s : strs) {
            int[] charCount = new int[26];
            for(char c : s.toCharArray()) {
                charCount[c - 'a']++;
            }
            String key = Arrays.toString(charCount);
            hm.putIfAbsent(key, new ArrayList<>());
            hm.get(key).add(s);
        }
        return new ArrayList<>(hm.values());

    }
}
