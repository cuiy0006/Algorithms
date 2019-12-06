// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        vector<int> people;
        for(int i = 0; i < n; ++i){
            people.push_back(i);
        }
        
        while(people.size() > 1){
            int a = people[people.size() - 1];
            people.pop_back();
            int b = people[people.size() - 1];
            people.pop_back();
            bool aKnowsB = knows(a, b);
            bool bKnowsA = knows(b, a);
            if(aKnowsB && !bKnowsA){
                people.push_back(b);
            }
            
            if(bKnowsA && !aKnowsB){
                people.push_back(a);
            }
        }
        
        if(people.size() == 0){
            return -1;
        }
        
        int cel = people[people.size() - 1];
        for(int i = 0; i < n; ++i){
            if(i == cel){
                continue;
            }
            if(knows(cel, i) || !knows(i, cel)){
                return -1;
            }
        }
        return cel;
    }
};
