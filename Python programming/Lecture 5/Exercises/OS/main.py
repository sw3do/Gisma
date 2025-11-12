import os


def main():
    current_folder = os.getcwd()
    print(f"Current Working Directory: {current_folder}")
    list_of_files = os.listdir(current_folder)
    for file in list_of_files:
        print(f"File Name: {file}, File Path: {os.path.join(current_folder, file)}")


if __name__ == "__main__":
    main()
