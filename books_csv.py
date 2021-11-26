import csv
import functions


def get_from_csv():
    try:
        result = []
        with open("books.csv", 'r') as f:
            reader = csv.DictReader(f)
            for c in reader:
                temp = {}
                for a, b in c.items():
                    temp[a] = b
                result.append(temp)
                # print("-----")
        return result
    except FileNotFoundError:
        return


def write_to_csv(d):
    with open("books.csv", 'w', newline='') as f:
        csvwriter = csv.writer(f)
        key = list(d[0].keys())
        csvwriter.writerow(key)
        for i in d:
            csvwriter.writerow(list(i.values()))
    return


def add_to_csv(data):
    get = get_from_csv()
    get.append(data)
    write_to_csv(get)
    return


def delete_to_csv(n):
    get = get_from_csv()
    get.remove(n)
    write_to_csv(get)
    return


if __name__ == "__main__":
    add_to_csv(functions.show(isbn=9788937853470))
