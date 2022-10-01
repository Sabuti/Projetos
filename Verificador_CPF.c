#include <stdio.h>
#include <stdlib.h>

int verificao1(int *cpf1){
    int soma1 = 0;

    for (int i = 1; i < 10; i++){
        soma1 += cpf1[i-1] * i; }

    soma1 = soma1 % 11; // para chegar no 1o digito verificador

    if(soma1 == 10){
        soma1 = 0;  }
    
    if (soma1 != cpf1[9]){  // verificando se o calculado é = ao fornecido pelo usuário
        printf("\n CPF invalido, tente novamente depois");
        return 0; }
    return 0; }

int verificao2(int *cpf2){
    int soma2 = 0;

    for (int i = 0; i < 10; i++){
        soma2 += cpf2[i] * i; }

    soma2 = soma2 % 11;

    if(soma2 == 10){
        soma2 = 0;  }

    if (soma2 != cpf2[10]){  // verificando se o calculado é = ao fornecido pelo usuário
        printf("\nCPF invalido, tente novamente depois");
        return 0; }
    return 0; }

int main(){
    int i, valor;
    int soma2 = 0;
    int lista_cpf[11];

    for (i = 0; i < 11; i++){ // recebendo os dados
        printf("Qual seu %i numero? ",i+1);
        scanf("%i", &valor);
        lista_cpf[i] = valor;
    }

    verificao1(lista_cpf); // fazendo a verificação 1

    verificao2(lista_cpf); // fazendo a verificação 2

    printf("\nParabens, seu CPF eh valido");
    
    return 0;
}