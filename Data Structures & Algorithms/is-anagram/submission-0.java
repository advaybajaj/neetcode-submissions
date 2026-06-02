class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n!=m) {
            return false;
        }

        HashMap<Character, Integer> set = new HashMap<Character, Integer>();
        for(int i=0; i<n; i++) {
            char ss = s.charAt(i);
            if(!(set.containsKey(ss))) {
                set.put(ss, 1);
            } else {
                set.put(ss, set.get(ss)+1);
            }
        }

        for(int i=0; i<m; i++) {
            char tt = t.charAt(i);
            if(!(set.containsKey(tt))) {
                return false;
            } else {
                if (set.get(tt)==1) {
                    set.remove(tt);
                } else {
                    set.put(tt, set.get(tt)-1);
                }
            }
        }

        return true;
    }
}
