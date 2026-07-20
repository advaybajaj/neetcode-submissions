class Solution {
    public int evalRPN(String[] tokens) {
        int answer = 0;
        Stack<Integer> s = new Stack<>();
        for (String item : tokens) {
            if(item.equals("+")) {
                int n1 = s.pop();
                int n2 = s.pop();
                s.push(n1+n2);
            } else if(item.equals("-")) {
                int n1 = s.pop();
                int n2 = s.pop();
                s.push(n2-n1);
            } else if(item.equals("*")) {
                int n1 = s.pop();
                int n2 = s.pop();
                s.push(n1*n2);
            } else if(item.equals("/")) {
                int n1 = s.pop();
                int n2 = s.pop();
                s.push(n2/n1);
            } else {
                s.push(Integer.valueOf(item));
            }
        }
        return s.pop();
    }
}
