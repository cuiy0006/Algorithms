class Vector2D {
public:
    Vector2D(vector<vector<int>>& v)
        : i(0),
          j(0),
          vec(v){
        while(i < vec.size() && vec[i].size() == 0){
            ++i;
        }
    }
    
    int next() {
        int res = vec[i][j];
        if(j == vec[i].size() - 1){
            j = 0;
            ++i;
            while(i < vec.size() && vec[i].size() == 0){
                ++i;
            }
        } else {
            j += 1;
        }
        return res;
    }
    
    bool hasNext() {
        if(i >= vec.size() || j >= vec[i].size()){
            return false;
        }
        return true;
    }
private:
    int i;
    int j;
    vector<vector<int>> vec;
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D* obj = new Vector2D(v);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
