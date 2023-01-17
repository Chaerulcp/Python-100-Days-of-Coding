# Tebak Angka

def guess_number():
    lower_bound = 1
    upper_bound = 100
    past_guesses = []
    # Dapatkan nomor pengguna
    number = int(input("Masukkan angka antara 1 dan 100 untuk ditebak oleh komputer: "))
    while True:
        # Dapatkan tebakan komputer
        guess = (lower_bound + upper_bound) // 2
        past_guesses.append(guess)
        if guess == number:
            print(f"Komputer menebak nomornya {len(past_guesses)} mencoba: {past_guesses}")
            break
        elif guess > number:
            upper_bound = guess
            print("Terlalu tinggi. Petunjuk: Jumlahnya lebih kecil dari atau sama dengan", upper_bound)
        else:
            lower_bound = guess
            print("Terlalu rendah. Petunjuk: Jumlahnya lebih tinggi dari atau sama dengan", lower_bound)

guess_number()
