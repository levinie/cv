import numpy as np
import cv2, os, shutil, time

def cap_save_video(save_dir, video_name = "out.mp4", video_time = 10):
    img_dir = os.path.join(save_dir, "img")
    start = time.time()
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.mkdir(save_dir)
    os.mkdir(img_dir)
    #
    cap = cv2.VideoCapture(0)
    count = 0
    while cap.isOpened():
        end = time.time()
        if end - start > video_time:
            break
        ret, frame = cap.read()
        if ret == True:
            count += 1
            cv2.imwrite("{img_dir}/{count}.jpg".format(img_dir = img_dir, count = str(count).zfill(15)), frame)
        else:
            break
    cap.release()
    #
    os.chdir(img_dir)
    os.system("ffmpeg -y -r 24 -i %15d.jpg {video_name}".format(video_name = video_name))
    shutil.move(os.path.join(img_dir, video_name), os.path.join(save_dir, video_name))

if __name__ == "__main__":
    cap_save_video("/home/levi/temp/cv/video/test")