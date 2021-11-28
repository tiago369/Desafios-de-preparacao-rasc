#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main(){
    string txt;
    cout << "Digite a palavra a ser permutada: ";
    cin >> txt;

    sort(txt.begin(), txt.end());
    do{
        cout << txt << endl;
    }while(next_permutation(txt.begin(), txt.end()));
    
    return 0;
}