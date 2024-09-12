# Vokalräkning
#Commit
def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    mening=input( ).lower()
    A_vokaler="aeiouyåäö"
    yes= sum(mening.count(vowel) for vowel in A_vokaler)
    print(yes)
    

if __name__ == "__main__":
    main()
