import json, os, io

encoding = "utf-8"


def read_json(path):
    with io.open(path, 'r', encoding="utf-8") as f:
        return json.load(f)


def read_file(path):
    with io.open(path, 'r', encoding="utf-8") as f:
        return f.read()


def save_json_file(path, new_data):
    with io.open(path, 'w', encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False)


def save_file(path, new_data):
    with io.open(path, 'w', encoding="utf-8") as f:
        f.write(new_data)


def list_files(path):
    return os.listdir(path)




"""
    Populate the kill_list

lettters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
kill_list = []

for file in list_files("./originals"):
    if file.startswith("cn") or file.startswith("ko") or file.startswith("ja") or file.startswith("bn") or file.startswith("el") or file.startswith("hi") or file.startswith("iw") or file.startswith("ka") or file.startswith("iw") or file.startswith("th") or file.startswith("ar"):
        words = read_json("./originals/" + file)
        print("Processing " + file)
        for i, word in enumerate(words):
            if word[0] in lettters or word[-1] in lettters:
                kill_list.append(i)

kill_list = list(set(kill_list))
kill_list.sort(reverse=True)
save_file("./kill_list.txt", str(kill_list))
"""



"""
    Kill words
kill_list = eval(read_file("./kill_list.txt"))
kill_list = list(set(kill_list))
kill_list.sort()
kill_list.reverse()

for file in list_files('./originals/'):
    file_path = './originals/' + file
    words = read_json(file_path)
    print(file_path, len(words))

    # for each of kill_list, remove it from words
    for word in kill_list:
        del words[word]

    save_json_file("./native/" + file, words)
"""








