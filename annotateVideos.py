import cv2 as cv
import numpy as np
import pdb
import glob
import os

def read_frames(video_path):
    frames = []
    cap = cv.VideoCapture(video_path)
    if cap.isOpened() is False:
        print("Error opening video stream or file")
        return frames

    while cap.isOpened():
        ret, frame = cap.read()  # Read the frame
        if ret is True:
            frames.append(frame)
        else:
            break
    cap.release()
    return frames


video_name = glob.glob('*.mp4')


colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 255, 255), (255, 0, 255)]


for name in video_name:
    frames = read_frames(name)
    video_extension_and_fourcc_dict = {'avi': cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                       'mp4': 0x7634706d}

########################## edit here
    txt_file1 = os.path.basename(name)[:-4] + '_out_ball_1.txt'
    txt_file2 = os.path.basename(name)[:-4] + '_out_ball_2.txt'
##########################################

    arr = np.loadtxt(txt_file1, np.int)
    arr = arr[1:]
    for line in arr:
        frame_idx = line[0]
        bbox = line[1:]
        bbox = [int(b) for b in bbox]
        cv.rectangle(frames[frame_idx], (bbox[0], bbox[1]), (bbox[2], bbox[3]), colors[0 % len(colors)], thickness=2)

    arr = np.loadtxt(txt_file2, np.int)
    arr = arr[1:]
    for line in arr:
        frame_idx = line[0]
        bbox = line[1:]
        bbox = [int(b) for b in bbox]
        cv.rectangle(frames[frame_idx], (bbox[0], bbox[1]), (bbox[2], bbox[3]), colors[1 % len(colors)], thickness=2)


    video_output_name = "%s_annotated.mp4" % name[:-4]
    output_video = cv.VideoWriter(video_output_name, video_extension_and_fourcc_dict["mp4"], 30,
                                  (frames[0].shape[1], frames[0].shape[0]))

    num_frames = len(frames)
    for i in range(0, num_frames):
        output_video.write(frames[i])

    output_video.release()
    print('written ' + video_output_name)
