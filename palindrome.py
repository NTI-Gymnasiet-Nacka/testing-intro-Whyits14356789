# Palindrome
#Commit-klar
def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    Rnd_word=input( )
    word=Rnd_word.strip()[::-1]

    if Rnd_word == word:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
