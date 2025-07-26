#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "kalman.c"

#define N 20

float noisy(float t) {
    return t + ((float)rand() / RAND_MAX) * 10.0f - 5.0f;
}

int main() {
    srand(42);
    float alt = 0.0f, vel = 0.0f, acc = 9.81f;
    float est0, est1;

    for (int i = 0; i < N; ++i) {
        vel += acc * 0.1f;
        alt += vel * 0.1f;
        float m = noisy(alt);
        filter_kalman(m, acc, &est0, &est1);
        printf("Step %2d | True: %7.2f | Measured: %7.2f | Estimated: %7.2f\n", i, alt, m, est0);
    }

    return 0;
}
