#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void factor (const long int &n, vector<int> & factors)
{
    int max = ceil(sqrt(n));

    for(int f = 2; f <= max; f++)
    {
        if(n == 2)
        {
            break;
        }
        if(n % f == 0)
        {
            factor(f, factors);
            factor(n / f, factors);
            return;
        }
    }

    factors.push_back(n);
}

int largest(vector<int> &list)
{
    int max = 0;

    for(auto x : list)
    {
        if(x > max)
        {
            max = x;
        }
    }

    return max;
}

int main()
{
    /*
    int n = 24;
    vector<int> factors;

    factor(n, factors); 

    for(auto x : factors)
    {
        cout << x << endl;
    }

    return 0;
    */
   long int n = 600851475143;

   vector<int> factors;
   
   factor(n, factors);

    cout << largest(factors) << endl;

    return 0;
}