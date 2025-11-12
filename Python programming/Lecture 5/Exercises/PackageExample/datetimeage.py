import datetime as dt


def main():
    while True:
        try:
            user_year = int(input("Enter a year: "))
            year = dt.datetime.today().year
            if year < user_year or year == user_year or user_year < 1:
                raise ValueError("Invalid year")
            print(year - user_year)
        except ValueError:
            print("Please enter a valid year")
        except KeyboardInterrupt:
            print("User interrupted")


if __name__ == "__main__":
    main()
