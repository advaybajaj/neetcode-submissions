class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length()!=t.length()) {
            return false;
        }

        HashMap<Character, Integer> set = new HashMap<Character, Integer>();
        for(int i=0; i<s.length(); i++) {
            if(!(set.containsKey(s.charAt(i)))) {
                set.put(s.charAt(i), 1);
            } else {
                set.put(s.charAt(i), set.get(s.charAt(i))+1);
            }
        }

        for(int i=0; i<t.length(); i++) {
            if(!(set.containsKey(t.charAt(i)))) {
                return false;
            } else {
                if (set.get(t.charAt(i))==1) {
                    set.remove(t.charAt(i));
                } else {
                    set.put(t.charAt(i), set.get(t.charAt(i))-1);
                }
            }
        }

        return true;
    }
}
