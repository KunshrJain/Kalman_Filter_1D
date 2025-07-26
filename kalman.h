#ifndef KALMAN_H
#define KALMAN_H

void filter_kalman(float noisy_alt, float acc, float* est_alt_out, float* est_vel_out);

#endif 
