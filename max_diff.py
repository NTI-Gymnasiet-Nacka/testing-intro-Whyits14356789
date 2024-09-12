# Största skillnad


def main(input_yes):
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    maximal_skillnad = list(map(int, input_yes.replace(" ", ",").split(",")))

    minsta_värde = min(maximal_skillnad)
    största_värde = max(maximal_skillnad)

    differens = största_värde - minsta_värde
    return differens


if __name__ == "__main__":
    input_yes = input("")
    diff = main(input_yes)
    print(diff)
