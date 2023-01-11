def calculate_molecular_dipole_moment(molar_mass, bond_polarizability, bond_length):
    return molar_mass * bond_polarizability * bond_length

molar_mass = 30.06  # dalam g/mol
bond_polarizability = 3.2  # dalam Å³
bond_length = 1.5  # dalam Å

result = calculate_molecular_dipole_moment(molar_mass, bond_polarizability, bond_length)
print("Molecular Dipole Moment : ",result," debye")
