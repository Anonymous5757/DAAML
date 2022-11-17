#include<stdio.h>
#include<iostream>

using namespace std;


int main()
{
int dp[100][100];

    for(int i=0;i<100;i++)
    dp[i][0]=0;

    for(int i=0;i<100;i++)
    dp[0][i]=0;

    
    int n;
    int W;

    int wt[n];
    int val[n];

for(int i=1;i<=n;i++)
    {

        for(int j=1;j<=W;j++)
        {
            if(wt[i-1]<=j)
            dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j- wt[i-1]]);
            else 
            dp[i][j]=dp[i-1][j];

        }

    }

    for(int i=0;i<=n;i++)
    for(int j=0;j<=W;j++)
        cout<<dp[i][j];





    cout<<dp[n][W];
}