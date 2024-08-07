#include <stdio.h>
#include <math.h>
int power(int a, int b, int p) {
    int res = 1;
    a = a % p;
    while (b > 0) {
        if (b & 1)
            res = (res * a) % p;
        b = b / 2;
        a = (a * a) % p;
    }
    return res;
}
int main() {
    int p, g, xa, xb, ya, yb, ka, kb;
    p = 7; 
    g = 3; 
    xa = 2;
    xb = 5;
    ya = power(g, xa, p);
    yb = power(g, xb, p);
    ka = power(yb, xa, p);
    kb = power(ya, xb, p);
    printf("Alice's secret key is %d\n", ka);
    printf("Bob's secret key is %d\n", kb);
    return 0;
}
