class Solution {
public:
    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) {
        set<pair<int,int>> nodes;
        pair<int,int> a=pair(start[0],start[1]);
        pair<int,int> b=pair(target[0],target[1]);
        nodes.insert(a);
        nodes.insert(b);
        for(int i=0;i<specialRoads.size();i++){
            auto road=specialRoads[i];
            int x1=road[0];
            int y1=road[1];
            int x2=road[2];
            int y2=road[3];
            pair<int,int> p=pair(x1,y1);
            pair<int,int> q=pair(x2,y2);
            nodes.insert(p);
            nodes.insert(q);
        }
        map<pair<int,int>, vector<pair<pair<int,int>,int>>> adjList;
        for(auto &p:nodes)
            for(auto &q:nodes){
                int dist=abs(p.first-q.first)+abs(p.second-q.second);
                adjList[p].push_back({q, dist});
                adjList[q].push_back({p, dist});
            }
        for(int i=0;i<specialRoads.size();i++){
            auto road=specialRoads[i];
            int x1=road[0];
            int y1=road[1];
            int x2=road[2];
            int y2=road[3];
            int c=road[4];
            pair<int,int> p=pair(x1,y1);
            pair<int,int> q=pair(x2,y2);
            for(auto &n:adjList[p])
                if(n.first==q)
                    n.second=min(n.second,c);
        }
        int n=nodes.size();
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        pq.push({0, a});
        map<pair<int,int>,int>distance;
        map<pair<int,int>,bool>visited;
        for(auto &i:nodes)
            distance[i]=INT_MAX;
        distance[a] = 0;
        while (!pq.empty()) {
            pair<int,int> u = pq.top().second;
            pq.pop();
            if(visited[u])
             continue;
            visited[u]=true;
            if(u==b)
                break;
            for(auto &v:adjList[u]){
                int weight = v.second;
                if (distance[v.first] > distance[u] + weight) {
                    distance[v.first] = distance[u] + weight;
                    pq.push({distance[v.first], v.first});
                }
            }
        }
        return distance[b];
    }
};