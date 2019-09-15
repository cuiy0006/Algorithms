class Solution {
public:
    string predictPartyVictory(string senate) {
        int r = 0;
        int d = 0;
        int d_cnt = 0;
        int r_cnt = 0;
        for(auto c : senate){
            if(c == 'R'){
                ++r_cnt;
            } else {
                ++d_cnt;
            }
        }
        while(true){
            for(int i = 0; i < senate.size(); ++i){
                if(senate[i] == 'R'){
                    if(d != 0){
                        --d;
                        senate[i] = '*';
                        --r_cnt;
                    } else {
                        ++r;
                    }
                } else if(senate[i] == 'D'){
                    if(r != 0){
                        --r;
                        senate[i] = '*';
                        --d_cnt;
                    } else {
                        ++d;
                    }
                }
            }
            if(d_cnt == 0){
                return "Radiant";
            } else if(r_cnt == 0){
                return "Dire";
            }
        }
        return "Radiant";
    }
};
