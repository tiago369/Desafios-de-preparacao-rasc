#include<iostream>

using namespace std;

class book{
    public:
        string title;
        string author;
        int pages;

        book(){
            title = "no title";
            author = "no author";
            pages = 0;
        }

        book(string atitle, string aauthor, int apages){
            title = atitle;
            author = aauthor;
            pages = apages;
        }
};

int main(){

    book book1("Harry p","Juscelino K. Rowling",1235), book2("senhor dos aneis","Tk", 789);

    cout << book1.title << endl;
    cout << book2.author << endl;

    return 0;
}