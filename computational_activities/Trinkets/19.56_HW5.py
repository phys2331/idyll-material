# Variables
emf = 7.8
r1 = 23
r2 = 41
r3 = 56

# Calculate
r1r2_equiv = (r1*r2)/(r1+r2)
equiv_all = r1r2_equiv + r3
I = emf/equiv_all

# Print
print("The resistance of r1 & r2 is", r1r2_equiv, "ohms")
print("The resistance of all 3 is", equiv_all, "ohms")
print("The current is", I, "A")
