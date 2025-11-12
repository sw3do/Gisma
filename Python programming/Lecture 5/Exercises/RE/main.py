import is_email


def main():
    try:
        while True:
            email_input = input("Enter email: ")
            if is_email.check_email(email_input):
                print("Email is valid")
                break
            else:
                print("Email is not valid")
    except KeyboardInterrupt:
        print("User interrupted")


if __name__ == "__main__":
    main()
