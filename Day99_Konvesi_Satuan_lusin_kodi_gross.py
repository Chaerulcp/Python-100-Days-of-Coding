# Program Konversi Satuan Lusin, Kodi, dan Gross python

def convert_units(value, unit_from, unit_to):
    if unit_from == "lusin":
        if unit_to == "kodi":
            return value * 12
        elif unit_to == "gross":
            return value * 144
    elif unit_from == "kodi":
        if unit_to == "lusin":
            return value / 12
        elif unit_to == "gross":
            return value * 12
    elif unit_from == "gross":
        if unit_to == "lusin":
            return value / 144
        elif unit_to == "kodi":
            return value / 12
    else:
        return None

# hasil function
print(convert_units(4, "lusin", "kodi")) # output: 48
print(convert_units(4, "lusin", "gross")) # output: 576
print(convert_units(48, "kodi", "lusin")) # output: 4
print(convert_units(48, "kodi", "gross")) # output: 576
print(convert_units(576, "gross", "lusin")) # output: 4
print(convert_units(576, "gross", "kodi")) # output: 48
