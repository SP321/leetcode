class UnionFind{
    vector<int>parent;
    vector<int>rank;
public:
    int n;
    UnionFind(int n){
        this->n=n;
        parent.resize(n+1);
        rank.resize(n+1);
        for(int i=0;i<=n;i++)
            parent[i]=i;
    }
    int find(int x){
        if(x!=parent[x])
            parent[x]=find(parent[x]);
        return parent[x];
    }
    
    int combine(int a,int b){
        a = find(a);
        b = find(b);
        if(a == b)
            return 0;
        if(rank[a] < rank[b]){
            parent[a] = b;
        }
        else if(rank[a] > rank[b]){
            parent[b] = a;
        }
        else{
            rank[a] += 1;
            parent[b] = a;
        }
        n-=1;
        return 1;
    }   
};
        
class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        UnionFind a(n);
        UnionFind b(n);
        int c=0;
        for( auto &x:edges){
            int t=x[0];
            int u=x[1];
            int v=x[2];
            if(t==3){
                int x=a.combine(u,v);
                int y=b.combine(u,v);
                if(x||y)
                    c++;
            }
        }
        for( auto &x:edges){
            int t=x[0];
            int u=x[1];
            int v=x[2];
            if(t==1)
                c+=a.combine(u,v);
            if(t==2)
                c+=b.combine(u,v);
        }
        if(a.n==1 && b.n==1)
            return edges.size()-c;
        return -1;
    }
};