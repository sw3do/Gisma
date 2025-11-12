import pickle


def save_db(data):
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)
        return data


def load_db():
    with open('data.pickle', 'rb') as f:
        return pickle.load(f)


def delete_db(value):
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
        if value is dict:
            del data[value]
        elif value is list:
            idx = data.index(value)
            del data[idx]
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
