#include<iostream>
using namespace std;

class chef{
    public:
        void galinha(){
            cout << "O chefe faz galinha\n";
        }
        void feijao(){
            cout << "O chef faz feijao\n";
        }
        void file(){
            cout << "o chef faz file a cavala\n";
        }
};

class italian_chef : public chef{
    public:
        void macarrao(){
            cout << "O chef faz macarrao\n";
        }
        void file(){
            cout << "o chef faz file a parmegiana\n";
        }
};

int main(){
    chef chef1;
    chef1.galinha();

    italian_chef italia1;
    italia1.galinha();


    return 0;
}