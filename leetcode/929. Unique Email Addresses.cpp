#include <unordered_set>
#include <string>
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        std::unordered_set<std::string> s;
        for(int i = 0; i < emails.size(); ++i){
            std::string email = emails[i];
            int at_pos = email.find('@');
            std::string second_half = email.substr(at_pos, email.size() - 1);
            std::string first_half = "";
            for(int j = 0; j < email.size(); ++j){
                if(email[j] == '.'){
                    continue;
                } else if(email[j] == '+' || email[j] == '@'){
                    break;
                }
                first_half += email[j];
            }
            s.emplace(first_half + second_half);
        }
        return s.size();
    }
};
