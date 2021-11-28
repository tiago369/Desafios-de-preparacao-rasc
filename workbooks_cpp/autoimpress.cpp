#include<fstream>
#include<iostream>
using namespace std;

int main(){
    fstream codigo;
    string linha;

    codigo.open ("autoimpress.cpp", fstream::in);

    if(codigo.is_open()){
        while(getline(codigo, linha)){
            cout << linha << endl;
        }
    }

    codigo.close();

    return 0;
}