import db


def main():
    print("Pickle User")

    data = [
        {
            "name": "Mert",
            "username": "sw3doo",
            "email": "sw3doo@gmail.com",
        },
        {
            "name": "Kerem",
            "username": "kerosh",
            "email": "keremaltun@gmail.com",
        },
        {
            "name": "Tuna Uygar Oflaş",
            "username": "oflas",
            "email": "oflastuna@gmail.com",
        }
    ]
    db.save_db(data)
    all_data = db.load_db()
    print(all_data)
    for item in all_data:
        print(item)


    all_data2 = db.load_db()
    print(all_data2)


if __name__ == '__main__':
    main()
