import os
import cv2
import json

json_path = 'data/train/json/'
img_path = 'data/train/img/'

save_path = 'data/train_dataset/test/'
labeltxt_path = 'data/train_dataset/label.txt'

## generate char string
str = ''
for json_file in os.listdir(json_path):
    f_json = open(json_path+json_file, encoding='utf-8')
    info = json.load(f_json)
    label_info = info['shapes']

    for i in range(len(label_info)):
        label_text = label_info[i]['label']
        for char in label_text:
            if char not in str:
                str += char

label_txt = open('data/train_dataset/char.txt', 'w', encoding='utf-8')
label_txt.write(str)
print(len(str))

## generate label img & txt
for json_file in os.listdir(json_path):
    f_json = open(json_path+json_file, encoding='utf-8')
    info = json.load(f_json)

    img_name = info['imagePath']
    img = cv2.imread(img_path+img_name)
    name = img_name.split('.')[0]

    label_info = info['shapes']

    print(img_name)

    for i in range(len(label_info)):
        label_txt = open(labeltxt_path, 'a', encoding='utf-8')

        points = label_info[i]['points']
        x0 = min(int(points[0][0]), int(points[1][0]), int(points[2][0]), int(points[3][0]))
        x1 = max(int(points[0][0]), int(points[1][0]), int(points[2][0]), int(points[3][0]))
        y0 = min(int(points[0][1]), int(points[1][1]), int(points[2][1]), int(points[3][1]))
        y1 = max(int(points[0][1]), int(points[1][1]), int(points[2][1]), int(points[3][1]))
        label_img = img[y0:y1, x0:x1]
        cv2.imwrite('{}{}_{}.jpg'.format(save_path, name, i), label_img)

        label_text = label_info[i]['label']
        label_txt.write('test/{}_{}.jpg'.format(name, i) + ' ' + label_text + '\n')


