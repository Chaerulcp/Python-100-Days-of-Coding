# Mengitung tegangan listrik

def calculate_voltage(current, resistance):
    voltage = current * resistance
    return voltage

current = 5  # dalam ampere
resistance = 10  # dalam ohm

result = calculate_voltage(current, resistance)
print("Tegangan: ",result," volt")
