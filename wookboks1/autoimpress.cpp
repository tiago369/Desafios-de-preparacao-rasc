#include<fstream>
#include<iostream>
using namespace std;

int main(){
    std::fstream fs;
    fs.open ("autoimpress.cpp", std::fstream::in | std::fstream::out | std::fstream::app);

    return 0;
}