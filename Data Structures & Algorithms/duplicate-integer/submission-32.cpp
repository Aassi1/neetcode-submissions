class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> duplicateSet;

        for (int num : nums) {
            if (duplicateSet.contains(num) ){
                return true;
            }
            duplicateSet.insert(num);
        }
        return false;
        
    }
};