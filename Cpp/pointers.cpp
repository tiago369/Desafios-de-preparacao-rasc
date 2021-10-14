#include<iostream>

using namespace std;

int main(){

    int age = 19;
    int *page = &age;
    double gpa = 2.7;
    double *pgpa = &gpa;
    string name = "mike";
    string *pname = &name;

    cout << "Age: " << &age << endl;
    cout << page << endl;
    cout << *page << endl;
    cout << *&age << endl;
    


    return 0;
}