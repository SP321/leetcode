class UndergroundSystem {
public:
    map<int, pair<string, int>> d;
    map<pair<string, string>, pair<int, int>> ans;
    UndergroundSystem() {
    }
    
    void checkIn(int id, string stationName, int t) {
        d[id]={stationName,t};
    }
    
    void checkOut(int id, string stationName, int t) {
        string start=d[id].first;
        int time=d[id].second;
        pair<string,string>route={start,stationName};
        ans[route].first += (t - time);
        ans[route].second += 1;
    }

    double getAverageTime(string startStation, string endStation) {
        pair<string, string> route = {startStation, endStation};
        return ((double) ans[route].first) / ans[route].second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */