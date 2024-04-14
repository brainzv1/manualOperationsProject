import os
import cv2
import shutil
import random

def extract_frames(video_path, output_dir, video_name, skip):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video - {video_path}")
        return
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    success, frame = cap.read()
    count = 1
    while success:
        if random.random() <= skip:
            frame_path = os.path.join(output_dir, f"img_{'{:05d}'.format(count)}.jpg")
            cv2.imwrite(frame_path, frame)

        success, frame = cap.read()
        count += 1

    cap.release()

def process_videos(data_dir, project_dir, annotation_files, output_dir, skip):
    # Delete existing train, val, test folders and create new ones
    for folder in ['train', 'val', 'test']:
        folder_path = os.path.join(output_dir, folder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)

    # Process videos for train, val, and test sets
    for set_type, annotation_file in annotation_files.items():
        with open(annotation_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                video_path, total_frames_str, label = line.strip().split()
                total_frames = int(total_frames_str)
                video_path = os.path.join(project_dir, video_path)
                video_name = os.path.splitext(os.path.basename(video_path))[0]  # Extract video name without extension

                output_subdir_path = os.path.join(output_dir, set_type, video_name)
                os.makedirs(output_subdir_path, exist_ok=True)

                # Copy video file to appropriate folder
                shutil.copy(video_path, output_subdir_path)

                # Extract frames
                extract_frames(video_path, output_subdir_path, video_name, skip)

# Function to get all video files from a directory
def get_video_files(directory):
    video_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.avi'):
                video_files.append(os.path.join(root, file))
    return video_files

current_path = os.getcwd()
project_directory = os.path.dirname(current_path)

data_directory = current_path + "\\" + r"mmaction2\DataSet\Data"
output_annotation_file = r"mmaction2\DataSet\annotation.txt"

annotation_files = {
    'train': r"mmaction2\DataSet\train.txt",
    'val': r"mmaction2\DataSet\val.txt",
    'test': r"mmaction2\DataSet\test.txt"
}
output_dir = current_path + "\\" + r"mmaction2\DataSet"
# Get all video files from the data directory
video_files = get_video_files(data_directory)

while True:
    try:
        user_input = int(input("What % of all frames do you want to keep?"))
        if 0 < user_input <= 100:
            skip_probability = 0.01 * user_input
            break
        else:
            print("Please enter a value between 1 and 100.")
    except ValueError:
        print("Please enter a valid integer.")

# Process videos using the annotation files
process_videos(data_directory, project_directory, annotation_files, output_dir, skip_probability)

