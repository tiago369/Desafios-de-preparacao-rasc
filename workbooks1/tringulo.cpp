#include<iostream>
#include<math.h>

using namespace std;

int fatorial(int n){
    int a = 1;
    if(n > 0){
        for(int i = n; i > 0; i--){
            a *= i;
        }
    }
    else{
        return 1;
    }
    return a;

}

int triangulo_de_pascal(int linha, int posicao_linha){
    int pascal;
    // verificar a validade dos numeros digitados
    if(linha == 0 && posicao_linha != 0) return 0;
    else if(linha > 0 && posicao_linha > linha+1) return 0;
    else if(linha < 0) return 0; 
    //calcular o valor da determinada posiçao
    if(linha == 0) return 1;
    pascal = fatorial(linha) / (fatorial(posicao_linha) * fatorial(linha-posicao_linha));
    return pascal;
}

int main(){

    int a, b;

    cout << "Calculadora de triangulo de pascal\n\n";
    cout << "*considere a primeira linha como 0 e a primeira posiçao com 0 tambem*\n\n";

    cout << "Insira a linha: ";
    cin >> a;
    cout << "Insira a posiçao do numero: ";
    cin >> b;

    cout << triangulo_de_pascal(a, b) << endl;

    return 0;
}