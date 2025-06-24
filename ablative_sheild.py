# Ablative shield burn time calculator

def calculate_burn_time(mass_total, ablation_rate):
    """
    Calculate the time of burn absorption for an ablative shield.

    Parameters:
    mass_total (float): Total mass of the ablative material (in kilograms).
    ablation_rate (float): Ablation rate (in kilograms per second).

    Returns:
    float: Time of burn absorption (in seconds).
    """
    if ablation_rate <= 0:
        raise ValueError("Ablation rate must be greater than zero.")
    
    # Time is simply the total mass divided by the ablation rate
    time = mass_total / ablation_rate
    return time

# Get user input
try:
    mass_total = float(input("Enter the total mass of the ablative material (in kilograms): "))
    ablation_rate = float(input("Enter the ablation rate (in kilograms per second): "))
    
    burn_time = calculate_burn_time(mass_total, ablation_rate)
    
    print(f"The burn absorption time is: {burn_time:.2f} seconds")
except ValueError as e:
    print(f"Invalid input: {e}")
