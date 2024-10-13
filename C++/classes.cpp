#include <iostream>
#include <string>


using namespace std;

class Dog
{
    private:
        string name;
        string breed;
        string color;
        int age;
        float weight;
    public:
        Dog(string n, string b, string c, int a, float w)
        {
            setName(n);
            setBreed(b);
            setColor(c);
            setAge(a);
            setWeight(w);
        }

        void setName(string n)
        {
            name = n;
        }
        void setBreed(string b)
        {
            breed = b;
        }
        void setColor(string c)
        {
            color = c;
        }
        void setAge(int a)
        {
            age = a;
        }
        void setWeight(float w)
        {
            weight = w;
        }

        string getName()
        {
            return name;
        } 
        string getBreed()
        {
            return breed;
        }
        string getColor()
        {
            return color;
        }
        int getAge()
        {
            return age;
        }
        float getWeight()
        {
            return weight;
        }
};

Dog dogFunction(Dog dog1, Dog dog2)
{
    if(dog1.getWeight() >= dog2.getWeight())
    {
        return dog1;
    }
    else
    {
        return dog2;
    }
}


string function(int x)
{
    return "hello";
}
string function(string x)
{
    return "world";
}
string function(int x, string y)
{
    return "hi";
}


int main()
{
    Dog dog1("Fido", "poodle", "black", 6, 45.2);
    Dog dog2("Spot", "golden retriever", "yellow", 3, 55.2);

// Dog dog3();

    int x = 5;
    cout << function(x) << endl;

    string y = "abc";
    cout << function(y) << endl;

    cout << function(x, y) << endl;


    Dog heavyDog = dogFunction(dog1, dog2);
    cout << heavyDog.getName() << endl;
    
    return 0;
}