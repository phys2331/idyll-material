#Import Libraries
from scipy import constants
import numpy as np
import math

# Given variables. CHANGE THESE TO MATCH YOURS!

h_box = 0.04     # Part 1
w_box = 0.03     # Part 1
l_box = 0.20     # Part 1
E_1a = 1300      # Part 1
E_2a = 1050      # Part 1
E_3a = 750       # Part 1

h_cyl = 0.05     # Part 2
l_cyl = 0.15     # Part 2
E_1b = 1600      # Part 2
E_2b = 1400      # Part 2
E_3b = 1200      # Part 2

h_ramp = 0.04    # Part 3
w_ramp = 0.05    # Part 3
l_ramp = 0.18    # Part 3
l_slope = 0.12   # Part 3
E_1c = 120       # Part 3
E_2c = 400       # Part 3
E_3c = 280       # Part 3
E_4c = 275       # Part 3
E_5c = 205       # Part 3

# Pre-Calculations Part 1

area_box_tb = w_box * l_box
area_box_fb = h_box * l_box
area_box_smallsides = h_box * w_box

theta_box_fblr = math.cos(math.radians(90))
theta_box_top = math.cos(math.radians(0))
theta_box_bottom = math.cos(math.radians(180))

# Pre-Calculations Part 2

area_cyl_lr = constants.pi * (h_cyl/2)**2
area_cyl_rect = l_cyl * (2 * constants.pi * h_cyl/2)

theta_right = math.cos(math.radians(0))
theta_left = math.cos(math.radians(180))
theta_sides = math.cos(math.radians(90))

# Pre-Calculations Part 3

area_ramp_left = h_ramp * w_ramp
area_ramp_right = w_ramp * l_slope

angle_ramp = np.arcsin(h_ramp/l_slope)


theta_ramp_left = math.cos(math.radians(180))
theta_ramp_right = math.cos(math.radians(90-np.degrees(angle_ramp)))
theta_ramp_sides = 0

# Calculate

flux_box_fb = E_2a * area_box_fb * theta_box_fblr
flux_box_lr = E_2a * area_box_smallsides * theta_box_fblr
flux_box_top = E_3a * area_box_tb * theta_box_top
flux_box_bottom = E_1a * area_box_tb * theta_box_bottom
flux_box_total = flux_box_fb + flux_box_lr + flux_box_top + flux_box_bottom
charge_box = flux_box_total * constants.epsilon_0

flux_cyl_sides = E_2b * area_cyl_rect * theta_sides
flux_cyl_right = E_3b * area_cyl_lr * theta_right
flux_cyl_left = E_1b * area_cyl_lr * theta_left
flux_cyl_total = flux_cyl_sides + flux_cyl_right + flux_cyl_left
charge_cyl = flux_cyl_total * constants.epsilon_0

flux_ramp_left = E_1c * area_ramp_left * theta_ramp_left
flux_ramp_right = E_2c * area_ramp_right * theta_ramp_right
flux_ramp_total = flux_ramp_left + flux_ramp_right
charge_ramp = flux_ramp_total * constants.epsilon_0

# Print answer

print("Part 1: The total charge in the box =", charge_box, "C")
print("Part 2: The total charge in the cylinder =", charge_cyl, "C")
print("Part 3: The total charge in the ramp box =", charge_ramp, "C")
print(flux_ramp_right)
