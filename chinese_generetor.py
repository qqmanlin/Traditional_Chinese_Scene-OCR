import json
import os

json_root = 'data/train/json/'
files = os.listdir(json_root)

txt_root = 'data/train/chinese.txt'
chinese_dict = []

for i in range(len(files)):
    name = files[i].split('.')[0]
    json_name = os.path.join(json_root, files[i])

    f_json = open(json_name, 'r', encoding='utf-8')
    f_txt = open(txt_root, 'a', encoding='utf-8')
    data = json.load(f_json)
    shapes = data['shapes']

    for j in range(len(shapes)):
        label = shapes[j]['label']
        if (label in chinese_dict) or (str(label).isdigit()) or str(label).isupper() or str(label).islower():
            continue
        elif len(label)==1:
            f_txt.write(str(label) + '\n')
            chinese_dict.append(label)
    f_json.close()

f_txt.close()