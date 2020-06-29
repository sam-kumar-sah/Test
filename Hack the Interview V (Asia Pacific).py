#Hack the Interview V (Asia Pacific)
'''
1. New Keyboard
2. The XOR problem
3. Jewel Game
4. Rerouting
'''

#1. New Keyboard
#include <bits/stdc++.h>

using namespace std;

typedef int in;
#define int long long

in main()
{
    int n;
    string s;
    cin >> s;
    n = s.size();
    stack<string> q;
    bool b1 = 0,num=0;
    string s1 = "",ans = "";
    for(int i = 0 ; i < n ; i ++){
        if(s[i] == '>'){
            q.push(s1);
            s1="";
            b1 = 0;
            continue;
        }
        if(s[i] == '<'){
            q.push(s1);
            b1 = 1;
            s1="";
            continue;
        }
        if(s[i]=='*')
        {
            if(b1){
                if(s1.size())
                    s1.pop_back();
            }
            else{
                if(ans.size())
                    ans.pop_back();
            }
            continue;
        }
        if(s[i]=='#')
        {
            num^=1;
            continue;
        }
        if(b1){
            if(isdigit(s[i]) && num)
                continue;
            s1.push_back(s[i]);
        }
        else{
            if(isdigit(s[i]) && num)
                continue;
            ans.push_back(s[i]);
        }
    }
    if(s1.size()){
        q.push(s1);
    }
    while(q.size()){
        cout << q.top();
        q.pop();
    }
    cout << ans << endl;
    return 0;
}


#2. The XOR problem

def maxXorValue(x,k):
    n=len(x)
    assert(1<=n and n<=1000)
    assert(0<=k and k<=n)
    res=''
    for i in range(n):
        if x[i]=='0' and k>0:
            k-=1
            res+='1'
        else:
            res+='0'
    return res

if __name__=='__main__':
    t=int(input().strip())
    assert(1<=t and t<=100)
    for i in range(t):
        s=input()
        k=int(input().strip())
        ans=maxXorValue(s,k)
        print(str(ans))

#3. Jewel Game

def getMaxScore(s):
    res=0
    assert(1<=len(s) and len(s)<=100000)
    buf=[0]*(len(s)+1)
    l=0
    for i in s:
        assert(i>='a' and i<='z')
        if l!=0 and buf[l]==i:
            res+=1
            l-=1
        else:
            l+=1
            buf[l]=i
    return res

if __name__=='__main__':
    t=int(input().strip())
    assert(1<=t and t<=10)
    for i in range(t):
        s=input()
        ans=getMaxScore(s)
        print(str(ans))

#4. Rerouting

import math
def solve(n,connection):

    assert 1<=n<=300000
    assert all(1<=i<=n for i in connection)
    vis=[0]*(n+1)
    ct=0
    col=0
    for i in range(1,n+1):
        if not vis[i]:
            cur=i
            col+=1
            while not vis[cur]:
                vis[cur]=col
                cur=connection[cur-1]
                ct+=col==vis[cur]
    ct-=any(i==connection[i-1] for i in range(1,n+1))
    return ct

if __name__=='__main__':
    n=int(input().strip())
    connection=list(map(int,input().rstrip().split()))
    result=solve(n,connection)
    print(str(result))
