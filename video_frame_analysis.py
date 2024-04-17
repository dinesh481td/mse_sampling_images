import cv2
import numpy as np
import os


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def calculate_mse_for_all_frame_pairs(video_name):
    cap = cv2.VideoCapture(video_name)

    if not cap.isOpened():
        print(f"Error opening video file: {video_name}")
        return None

    ret, current_frame = cap.read()
    if not ret:
        print(f"Error reading first frame in video: {video_name}")
        return None

    previous_frame = current_frame
    mse_values = []
    while cap.isOpened():
        mse_value = mse(current_frame, previous_frame)
        mse_values.append(mse_value)

        previous_frame = current_frame.copy()
        ret, current_frame = cap.read()

        if not ret:
            break

    if len(mse_values) == 0:
        print(f"No MSE values calculated for video: {video_name}")
        return None

    average_mse = np.mean(mse_values)
    return average_mse


def key_frames(video_name, average_mse, no_frames_to_skip, image_folder):
    if average_mse is None:
        print(
            f"Cannot extract key frames from video: {video_name} due to invalid average MSE"
        )
        return

    cap = cv2.VideoCapture(video_name)
    ret, current_frame = cap.read()
    if not ret:
        print(f"Error reading first frame in video: {video_name}")
        return

    previous_frame = current_frame
    count = 1
    img_count = 0
    while cap.isOpened():

        mse_value = mse(current_frame, previous_frame)

        if mse_value > average_mse:
            count += 1
        if img_count <= 5:
            if count % no_frames_to_skip == 0:
                img_name = video_name.split("_")[-1] + f"_keyframe_{count}.jpg"
                success = cv2.imwrite(
                    os.path.join(image_folder, img_name), current_frame
                )
                if not success:
                    print(f"Failed to save image keyframe_{count}.jpg")
                img_count += 1
        previous_frame = current_frame.copy()
        ret, current_frame = cap.read()

        if not ret:
            break

    cap.release()


image_folder = r".\images"
os.makedirs(image_folder, exist_ok=True)
video_folder = r".\videos"
for i in os.listdir(video_folder):
    if i.endswith(".mp4"):
        video_name = os.path.join(video_folder, i)
        average_mse = calculate_mse_for_all_frame_pairs(video_name)
        no_frames_to_skip = 2
        key_frames(video_name, average_mse, no_frames_to_skip, image_folder)
