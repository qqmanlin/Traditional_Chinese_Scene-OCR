import json
import os
import numpy as np
import cv2

json_root = 'data/train/json/'
txt_root = 'data/train/txt/'
files = os.listdir(json_root)
obj_names = 'data/train/obj.names'
f_names = open(obj_names, 'a')
names = []

print(len(files))
for i in range(len(files)):
    name = files[i].split('.')[0]
    json_name = os.path.join(json_root, files[i])
    txt_name = os.path.join(txt_root, name+'.txt')
    f_json = open(json_name, 'r', encoding='utf-8')
    f_txt = open(txt_name, 'w')
    data = json.load(f_json)
    shapes = data['shapes']
    ww = float(data['imageWidth'])
    hh = float(data['imageHeight'])

    for j in range(len(shapes)):

        if shapes[j]['group_id'] == 255:
            shapes[j]['group_id'] = 6
        # if shapes[j]['group_id'] in names:
        #     pass
        # else:
        #     f_names.write(str(shapes[j]['group_id']) + '\n')
        #     names.append(shapes[j]['group_id'])
        if shapes[j]['label']=='' or shapes[j]['label']==' ':
            continue
        # print(shapes[j]['label'])

        points = shapes[j]['points']
        points = np.array(points)
        xs = points[:, 0].astype('float')
        ys = points[:, 1].astype('float')
        x_max = xs.max()
        x_min = xs.min()
        y_max = ys.max()
        y_min = ys.min()
        x_center = (x_min + x_max)/2
        y_center = (y_min + y_max)/2
        w = x_max - x_min
        h = y_max - y_min
        f_txt.write(str(shapes[j]['group_id']) + ' ')
        f_txt.write(str(x_center / ww) + ' ')
        f_txt.write(str(y_center / hh) + ' ')
        f_txt.write(str(w / ww) + ' ')
        f_txt.write(str(h / hh) + '\n')

    f_txt.close()
    f_json.close()
f_names.close()
