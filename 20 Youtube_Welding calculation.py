import math
import matplotlib.pyplot as plt

def calculate_stresses(forces, moments, area, inertia, section_modulus):

    # Extract inputs
    Fx, Fy, Fz = forces['Fx'], forces['Fy'], forces['Fz']
    Mx, My, Mz = moments['Mx'], moments['My'], moments['Mz']
    Wx, Wy, Wz = section_modulus['Wx'], section_modulus['Wy'], section_modulus['Wz']

    # Tensile stress (Normal Stress)
    tensile_stress = Fz / area
    # Shear stress (Due to shear forces)
    shear_stress = math.sqrt((Fx / area)**2 + (Fy / area)**2)

    # Bending stresses
    bending_stress_x = Mx / Wx
    bending_stress_y = My / Wy
    bending_stress_z = Mz / Wz
    # Combine bending stresses (resultant bending stress)
    bending_stress = math.sqrt(bending_stress_x**2 + bending_stress_y**2 + bending_stress_z**2)

    # Equivalent stress (Von Mises criterion)
    equivalent_stress = math.sqrt(tensile_stress**2 + 3 * shear_stress**2 + bending_stress**2)

    return {
        'Tensile Stress': tensile_stress,
        'Shear Stress': shear_stress,
        'Bending Stress': bending_stress,
        'Equivalent Stress': equivalent_stress
    }

def visualize_square_profile(width, height, Throat_thk):
    plt.figure(figsize=(6, 6))
    plt.plot([-width/2, width/2, width/2, -width/2, -width/2], [-height/2, -height/2, height/2, height/2, -height/2], 'r-', linewidth=3, label='Weld')
    plt.plot([-(width+Throat_thk)/2, (width+Throat_thk)/2, (width+Throat_thk)/2, -(width+Throat_thk)/2, -(width+Throat_thk)/2], [-(height+Throat_thk)/2, -(height+Throat_thk)/2, (height+Throat_thk)/2, (height+Throat_thk)/2, -(height+Throat_thk)/2], 'r-', linewidth=3)
    plt.fill([-(width+Throat_thk)/2, (width+Throat_thk)/2, (width+Throat_thk)/2, -(width+Throat_thk)/2, -(width+Throat_thk)/2], [-(height+Throat_thk)/2, -(height+Throat_thk)/2, (height+Throat_thk)/2, (height+Throat_thk)/2, -(height+Throat_thk)/2], color='red', alpha=1)
    plt.fill([-width/2, width/2, width/2, -width/2, -width/2], [-height/2, -height/2, height/2, height/2, -height/2], color='blue', alpha=1, label='Profile')
    plt.title(f"Square Profile: {width}mm x {height}mm")
    plt.xlabel("Width (mm)")
    plt.ylabel("Height (mm)")
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

def calculate_square_profile_weld_properties(width, height, Throat_thk):

    area = ((width+2*Throat_thk) * (height+2*Throat_thk)) - (width * height)
    Ix = (((width+2*Throat_thk) * (height+2*Throat_thk)**3) / 12)-((width * height**3) / 12)
    Iy = ((height+2*Throat_thk) * (width+2*Throat_thk)**3) / 12
    Iz = Ix + Iy  # Polar moment of inertia for square cross-section
    Wx = Ix / ((height+2*Throat_thk) / 2)
    Wy = Iy / ((width+2*Throat_thk) / 2)
    Wz = Iz / (max(width, height) / 2)

    return {
        'area': area,
        'inertia': {'Ix': Ix, 'Iy': Iy, 'Iz': Iz},
        'section_modulus': {'Wx': Wx, 'Wy': Wy, 'Wz': Wz}
    }


# Input forces and moments
forces = {'Fx': 1e5, 'Fy': 1e5, 'Fz': 1e5}  # in Newtons
moments = {'Mx': 2e5, 'My': 2e5, 'Mz': 2e5}  # in Newton-Millimetre

# User input for square profile
Input_width = 100  # in Millimetre
Input_height = 200  # in Millimetre
Throat_thk = 5  # in Millimetre

# Calculate properties for the square profile
properties = calculate_square_profile_weld_properties(Input_width, Input_height,Throat_thk)

area = properties['area']
inertia = properties['inertia']
section_modulus = properties['section_modulus']

print("Section Properties:")
print(f"Area: {area:.2f} mm^2")
print(f"Inertia (Ix): {inertia['Ix']:.3e} mm^4")
print(f"Inertia (Iy): {inertia['Iy']:.3e} mm^4")
print(f"Inertia (Iz): {inertia['Iz']:.3e} mm^4")
print(f"Section Modulus (Wx): {section_modulus['Wx']:.3e} mm^3")
print(f"Section Modulus (Wy): {section_modulus['Wy']:.3e} mm^3")
print(f"Section Modulus (Wz): {section_modulus['Wz']:.3e} mm^3")

# Calculate stresses
stresses = calculate_stresses(forces, moments, area, inertia, section_modulus)

for stress_type, value in stresses.items():
    print(f"{stress_type}: {value:.2f} MPa")

visualize_square_profile(Input_width, Input_height, Throat_thk)
