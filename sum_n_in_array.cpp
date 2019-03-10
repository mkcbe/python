#include<iostream>
using namespace std;
main()
{
    int n,k,arry[10000],sum;
    cin>>n>>k;
    for(int i=0;i<n;i++)
        cin>>arry[i];
    for(int i=0;i<k;i++)
        sum+=arry[i];
    cout<<sum;
}
