#include <vector>
#include <string>

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        std::vector<string> res;
        for(int i = 1; i <= n; ++i){
            bool three = i % 3 == 0;
            bool five = i % 5 == 0;
            if(three && five){
                res.push_back("FizzBuzz");
            } else if(three) {
                res.push_back("Fizz");
            } else if(five) {
                res.push_back("Buzz");
            } else {
                res.push_back(to_string(i));
            }
        }
        return res;
    }
};
