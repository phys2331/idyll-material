import numpy as np
from scipy import constants

# Assign the charges to variables
q1 = -5.5*10**-6
q2 = 6.5*10**-6
q3 = -7.5*10**-6

# Assign the locations to variables - convert cm to meters
q1_loc = np.array([0, 0.03, 0])
q2_loc = np.array([0.04, 0.03, 0])
q3_loc = np.array([0.04, 0, 0])
a_loc = np.array([0, 0, 0])

k = 1/(4*np.pi*constants.epsilon_0)

# E at Q3 due to Q1

r_vec_q3q1 = q3_loc - q1_loc
r_hat_q3q1 = r_vec_q3q1/np.linalg.norm(r_vec_q3q1)
E_1 = ((k * q1) / (np.linalg.norm(r_vec_q3q1)**2)) * r_hat_q3q1

# E at Q3 due to Q2

r_vec_q3q2 = q3_loc - q2_loc
r_hat_q3q2 = r_vec_q3q2/np.linalg.norm(r_vec_q3q2)
E_2 = ((k * q2) / (np.linalg.norm(r_vec_q3q2)**2)) * r_hat_q3q2

# E net at Q3 and F net on Q3

E_net_Q3 = E_1 + E_2
F_net_Q3 = q3*E_net_Q3

# E at A due to Q1

r_vec_aq1 = a_loc - q1_loc
r_hat_aq1 = r_vec_aq1/np.linalg.norm(r_vec_aq1)
E_3 = ((k * q1) / (np.linalg.norm(r_vec_aq1)**2)) * r_hat_aq1

# E at A due to Q2

r_vec_aq2 = a_loc - q2_loc
r_hat_aq2 = r_vec_aq2/np.linalg.norm(r_vec_aq2)
E_4 = ((k * q2) / (np.linalg.norm(r_vec_aq2)**2)) * r_hat_aq2

# E at A due to Q3

r_vec_aq3 = a_loc - q3_loc
r_hat_aq3 = r_vec_aq3/np.linalg.norm(r_vec_aq3)
E_5 = ((k * q3) / (np.linalg.norm(r_vec_aq3)**2)) * r_hat_aq3

# E net at A and F net on A with charge

A_charge = -3*10**-9
E_net_A = E_3 + E_4 + E_5
F_net_A = A_charge*E_net_A

# Print the answers

print("a)", list(E_1), "N/C")
print("b)", list(E_2), "N/C")
print("c)", list(E_net_Q3), "N/C")
print("d)", list(F_net_Q3), "N")
print("e)", list(E_3), "N/C")
print("f)", list(E_4), "N/C")
print("g)", list(E_5), "N/C")
print("h)", list(E_net_A), "N/C")
print("i)", list(F_net_A), "N")
