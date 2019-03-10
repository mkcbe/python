#include<iostream>
using namespace std;
main()
{
    int n,k,a[1000],sum;
    cin>>n>>k;
    if(n>0)
    {
        for(int i=0;i<n;i++)
            cin>>a[i];
        if(k>0)
        {
            for(int i=0;i<k;i++)
                sum+=a[i];
            cout<<sum;
        }
    }
}
