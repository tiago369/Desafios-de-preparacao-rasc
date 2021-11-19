#include<iostream>
using namespace std;

void permute_rec(int n ,string txt){
    int i, a;
    char aux;


    if(n <= 1){
        cout << txt << endl;
    }
    else{   
        //cout << txt << endl;
        
        for(i = 0; i < n; i++){
            permute_rec(n-1, txt);
            if(n % 2 == 0){
                //cout << txt << endl;
                aux = txt[i];
                txt[i] = txt[n-1];
                txt[n-1] = aux;
            }
            else{
                //cout << txt << endl;
                aux = txt[0];
                txt[0] = txt[n-1];
                txt[n-1] = aux;
            }
            permute_rec(n-1, txt);
            cout << txt << endl;
        }   
    }
}

void permute_non_rec(int n, string txt){
    int c[n], i;
    char aux;

    for(i = 0; i < n; i++){
        c[i] = 0;
    }
    
    cout << txt << endl;

    i = 0;
    while(i < n){
        if(c[i] < i){
            if(n % 2 == 0){
                //cout << txt << endl;
                aux = txt[i];
                txt[i] = txt[n-1];
                txt[n-1] = aux;
            }
            else{
                //cout << txt << endl;
                aux = txt[0];
                txt[0] = txt[n-1];
                txt[n-1] = aux;
            }
            cout << txt << endl;
            c[i]++;
            i = 0;
        }
        else{
            c[i]=0;
            i++;
        }
    }
}

void permute(string txt){
    int n;
    n = txt.length();
    permute_non_rec(n, txt);
}

int main(){
    
    string txt;
    getline(cin, txt);
    permute(txt);

    /*
    int y;
    cin >> y;
    cout << fatorial(y);*/


    return 0;
}