#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    for (int x = 0; x < t; x++) {
        cin >> n; 
        vector<int> nums;
        int temp;
        int max_num = 0;
        for (int i = 0; i < n; i++) {
            cin >> temp;
            nums.push_back(temp);
            max_num = max(max_num, temp);
        }
        int q = nums[n - 1];
        int k = 0;
        while (q != max_num) {
            k += 1;
            vector<int> new_arr;
            for (auto num : nums) {
                if (num > q) {
                    new_arr.push_back(num);
                }
            }
            nums.clear();
            for (auto num : new_arr) {
                nums.push_back(num);
            }
            q = new_arr[new_arr.size() - 1];
        }
        cout << k << endl;
    }
    
    return 0;
}
