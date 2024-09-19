#include <iostream>
#include <string>


using namespace std;

class Dog
{
    private:
        string breed;
        string color;
        int age;
        float weight;
    public:
        Dog(string b, string c, int a, float w)
        {
            this -> setBreed(b);
            this -> setColor(c);
            this -> setAge(a);
            this -> setWeight(w);
        }

        void setBreed(string b)
        {
            this -> breed = b;
        }
        void setColor(string c)
        {
            this -> color = c;
        }
        void setAge(int a)
        {
            this -> age = a;
        }
        void setWeight(float w)
        {
            this -> weight = w;
        }

        string getBreed()
        {
            return this -> breed;
        }
        string getColor()
        {
            return this -> color;
        }
        int getAge()
        {
            return this -> age;
        }
        float getWeight()
        {
            return this -> weight;
        }
};




int main()
{
    Dog dog1("poodle", "black", 6, 45.2);
    return 0;
}