class Solution {
public:
    bool isAnagram(string s, string t) {

        std::vector<int> duplicateArray(26,0);

        if (s.length() != t.length()){
            return false;
        }

        for (char letter: s){
            int index = letter - 'a';
            duplicateArray[index]++;
        }
        for (char letter: t){
            int index = letter - 'a';
            duplicateArray[index]--;
        }

        for (int num : duplicateArray){
            if (num != 0){
                return false;
            }
        }
        return true;
        
    }
};
