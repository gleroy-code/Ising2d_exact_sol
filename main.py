import numpy as np
import matplotlib.pyplot as plt
from energy import energy
import math

def main():
    #critical parameter
    x_c = 2 / math.log(1+math.sqrt(2))

    # Define the range of x values
    x_values = np.linspace(0.4, 4, 1000)

    # Calculate the corresponding energy values using the imported function
    energy_values = [energy(x) for x in x_values]

    # Plot the energy function
    plt.plot(x_values, energy_values, label='Energy Function')

    # Add a red vertical line at x = x_c
    plt.axvline(x_c, color='red', linestyle='--', label=f'$x_c={x_c}$')

    plt.xlabel('$k_BT/J$')
    plt.ylabel('$\\frac{E}{JN}$')
    plt.title('Energy density for 2D Ising Model with PDB in $N\\rightarrow \\infty$')
    plt.legend()
    
     # Save x and y values to a text file
    data = np.column_stack((x_values, energy_values))
    np.savetxt('energy_data.txt', data, header='x_values energy_values', comments='')

    
    plt.show()

    
    
if __name__ == "__main__":
    main()