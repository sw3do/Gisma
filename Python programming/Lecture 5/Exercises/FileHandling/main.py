def main():

    text = """We learn Python.
GISMA is our university.
Cool!
We like both Python and GISMA.
"""
    with open("text.txt", "w") as file:
        file.write(text)


    with open("text.txt", "r") as file:
        content = file.read()


    new_content = content.replace("like", "LIKE")

    with open("text.txt", "w") as file:
        file.write(new_content)

    with open("text.txt", "r") as file:
        content = file.read()



if __name__ == "__main__":
    main()
