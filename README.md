# Video Processing with Mean Squared Error (MSE)

This repository contains a Python script for video processing. The script reads video files, calculates the Mean Squared Error (MSE) between consecutive frames, and extracts key frames based on the calculated MSE.

## Dependencies

The script depends on the following Python libraries:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- os

You can install these dependencies using pip:
```bash
pip install -r requirements.txt
```

## Usage

The script contains three main functions:

1. `mse(imageA, imageB)`: This function calculates the Mean Squared Error (MSE) between two images. It's a measure of the differences between the two images.

2. `calculate_mse_for_all_frame_pairs(video_name)`: This function calculates the MSE for all pairs of consecutive frames in a video. It opens the video file, reads the frames one by one, and calculates the MSE between each pair of consecutive frames. The function returns the average MSE for all frame pairs.

3. `key_frames(video_name, average_mse, no_frames_to_skip, image_folder)`: This function extracts key frames from a video. It reads the video file, compares the MSE of each frame pair with the average MSE, and if the MSE of a frame pair is greater than the average, it saves the current frame as a key frame. The function skips a specified number of frames between each key frame extraction.

To use the script, you need to specify the video files to process and the image folder to save the key frames. The script reads all the .mp4 files in a video folder, calculates the average MSE for each video, and extracts key frames from each video. The key frames are saved in the image folder.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
