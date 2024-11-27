#include <string>
#include <iostream>
#include <array>

using namespace std;
void printHello()
{
    cout << "Hello" << endl;
}

int add(int x, int y)
{
    x = 2;
    y = 3;
    return x + y;
}

int addRef(int &x, int &y)
{
    x = 2;
    y = 3;
}

int addConstRef(const int &x, const int &y)
{
    
}
int main()
{
    int x = 5;
    int y = 2;
    cout << (x / y) << endl;
  
    float a = 5;
    float b = 2;
    cout << (a / b) << endl;

    double q = 0.000543;

    char zard = 'c';

    string message = "Hello World";

    array<int, 5> arr = {1, 2, 3, 4, 5};

    x = static_cast<float>(x);
    
    float z = static_cast<float>(x);
    cout << z / 2 << endl;


    for(int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
    }
    cout << endl;

    for(auto x : arr)
    {
        cout << x;
    }
    cout << endl;

    while(true)
    {
        break;
    }

    int m = 6;
    int n = 7;

    int sum = add(m, n);


    return 0;
}