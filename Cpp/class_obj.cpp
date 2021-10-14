#include<iostream>

using namespace std;

class book{
    public:
        string title;
        string author;
        int pages;
};

int main(){

    book book1, book2;
    
    book1.title = "Harry p";
    book1.author = "Juscelino K. Rowling";
    book1.pages = 1235;

    book1.title = "senhor dos aneis";
    book1.author = "Tk";
    book1.pages = 789;

    cout << book1.title << endl;
    cout << book2.author << endl;

    return 0;
}