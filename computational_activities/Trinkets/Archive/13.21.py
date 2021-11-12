import numpy as np

E_field = np.array([7000, 7000, 0])
particle_charge = -6*10**-9

E_hat = E_field/np.linalg.norm(E_field)
Force = particle_charge*E_field
F_hat = Force/np.linalg.norm(Force)

print("E_hat:", list(np.round(E_hat,10)))
print("F_vec:", list(np.round(Force,10)))
print("F_hat:", list(np.round(F_hat,10)))
