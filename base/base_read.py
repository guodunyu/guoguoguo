import yaml

def readfile():
    with open("./data/data.yaml", 'r', encoding="utf-8") as f:
        data = yaml.load(f)["test001"]
        data_list = []
        for i in data:
            data_list.append(data[i])
        print(data_list)
        return data_list

if __name__ == '__main__':
    readfile()