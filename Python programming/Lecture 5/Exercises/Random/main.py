from random_probability import chance


def main():
    try:
        for i in range(10):
            print(chance(0.3))
    except ValueError:
        print("Please enter a number between 0 and 1")


if __name__ == "__main__":
    main()
