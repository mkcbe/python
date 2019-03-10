#include<iostream>
using namespace std;
main()
{
    int n,k,a[1000],sum;
    cin>>n>>k;
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<k;i++)
        sum+=a[i];
    cout<<sum;
}
