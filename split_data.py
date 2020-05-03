import json

if __name__=="__main__":


    with open('./data/train.json') as json_file:
        json_data = json.load(json_file)

    print(json_data[:10])





