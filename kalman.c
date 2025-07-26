#include "kalman.h"

static float x0 = 0.0f, x1 = 0.0f;
static float p00 = 1.0f, p01 = 0.0f, p10 = 0.0f, p11 = 1.0f;

static const float dt = 0.1f;
static const float q = 0.01f;
static const float r = 10.0f;

void filter_kalman(float m, float a, float* est0, float* est1) {
   

    float t00 = p00 + dt * (p10 + p01 + dt * p11) + q;
    float t01 = p01 + dt * p11;
    float t10 = p10 + dt * p11;
    float t11 = p11 + q;

    p00 = t00; p01 = t01; p10 = t10; p11 = t11;

    float y = m - x0;
    float s = p00 + r;
    float k0 = p00 / s;
    float k1 = p10 / s;

    x0 += k0 * y;
    x1 += k1 * y;

    float np00 = (1.0f - k0) * p00;
    float np01 = (1.0f - k0) * p01;
    float np10 = -k1 * p00 + p10;
    float np11 = -k1 * p01 + p11;

    p00 = np00; p01 = np01; p10 = np10; p11 = np11;

    *est0 = x0;
    *est1 = x1;
}
