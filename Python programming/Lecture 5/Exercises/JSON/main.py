import db

def main():
    print("JSON DB")
    data = {
        "name": "Mert",
        "username": "sw3doo",
        "email": "sw3doo@gmail.com",
    }
    db.save_data(data)
    after_Save = db.load_data()
    print(after_Save)

if __name__ == '__main__':
    main()
