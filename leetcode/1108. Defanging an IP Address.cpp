#include <vector>
#include <sstream>

class Solution {
public:
    string defangIPaddr(string address) {
        std::stringstream ss(address);
        std::string item;
        std::string res;
        bool first = true;
        while(std::getline(ss, item, '.')){
            if(first){
                res = item;
                first = false;
            } else {
                res += "[.]" + item;
            }
        }
        return res;
    }
};
