#include <stdio.h>
#include <stdlib.h>

int main(){
    int i;
    int escolha1, escolha2;
    printf("De quanto vc quer sair? ");
    scanf("%i", &escolha1);
    printf("De quanto vc quer chegar? ");
    scanf("%i", &escolha2);
    for (i=escolha1; i<escolha2; i++){
        printf("%i \n", i);
    }
    return 0;
}
