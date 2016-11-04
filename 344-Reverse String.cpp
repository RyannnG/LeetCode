class Solution {
public:
    string reverseString(string s) {
        for (int l = 0, r = s.size() -1; l < r; l++, r--)
        {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
        }
        return s;
    }
};