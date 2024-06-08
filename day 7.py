import re

def validasi_email(email):
    # Pola regex untuk memvalidasi format email
    pola = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pola, email):
        return True
    return False

def main():
    email = input("Masukkan alamat email: ")
    
    if validasi_email(email):
        print(f"Alamat email '{email}' valid.")
    else:
        print(f"Alamat email '{email}' tidak valid.")

if __name__ == "__main__":
    main()
