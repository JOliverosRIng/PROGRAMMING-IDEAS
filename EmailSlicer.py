def main():
    emailInput = input("Enter the email to split: ")

    (username, domain) = emailInput.split("@")
    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Email domain: {domain}")
    print(f"Web Extension: {extension}")
    print("------------------------------->")


while True:
    print("Welcome to Email Slicer\n")
    main()
