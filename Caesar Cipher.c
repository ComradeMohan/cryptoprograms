#include <stdio.h>
#include <string.h>
void encrypt(char text[], int s) {
    for (int i = 0; i < strlen(text); i++) {
        if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] = (text[i] - 'a' + s) % 26 + 'a';
        } else if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = (text[i] - 'A' + s) % 26 + 'A';
        }
    }
}
int main() {
    char text[100];
    int s;
    printf("Enter the text: ");
    gets(text);
    printf("Enter the shift: ");
    scanf("%d", &s);
    encrypt(text, s);
    printf("Encrypted text: %s\n", text);
    encrypt(text, 26-s);
    printf("Decrypted text: %s\n", text);
    return 0;
}
// Function to decrypt the text
//void decrypt(char text[], int s) {
//    for (int i = 0; i < strlen(text); i++) {
//        if (text[i] >= 'a' && text[i] <= 'z') {
//            text[i] = (text[i] - 'a' - s + 26) % 26 + 'a';
//        } else if (text[i] >= 'A' && text[i] <= 'Z') {
//            text[i] = (text[i] - 'A' - s + 26) % 26 + 'A';
//        }
//    }
//}
