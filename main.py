import os
import cv2
import pandas as pd


def get_filepath(path):
    paths = []
    for filepath, dirpath, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(filepath, filename)
            paths.append(path)
    return paths


def get_vedio_height_width(filename, file_level):
    item = {}
    tmp = [f'{"一二三四五六七八九十"[i]}级目录名' for i in range(file_level)]
    for i in range(file_level):
        if i < len(filename.split('/'))-1:
            item[tmp[i]] = filename.split('/')[i]
            continue
        item[tmp[i]] = ''
    cap = cv2.VideoCapture(filename)
    item['视频名'] = filename.split('/')[-1]
    item['fps'] = int(cap.get(5))
    time = cap.get(7)/cap.get(5)
    item['时长'] = '%02d:%02d:%02d' % (int(time//3600), int(time//60), int(time%60))
    item['清晰度'] = '%sx%s' % (int(cap.get(3)), int(cap.get(4)))
    return item


if __name__ == '__main__':
    file_level = 6  #目录级别
    path = 'info-example'  #视频文件目录
    filepaths = get_filepath(path)
    items = []
    for filepath in filepaths:
        item = get_vedio_height_width(filepath, file_level)
        items.append(item)
    df = pd.DataFrame(items)
    df.to_csv('data.csv', index=False)
    print('done')