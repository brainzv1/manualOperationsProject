import os
import cv2


def get_total_frames(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video - {video_path}")
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()
    return total_frames

def extract_label_from_path(video_path):
    parent_folder = os.path.basename(os.path.dirname(video_path))
    return parent_folder

def create_annotation_file(data_dir, project_dir, annotation_file):
    with open(annotation_file, 'w') as f:
        for root, dirs, files in os.walk(data_dir):
            for video_file in files:
                if video_file.endswith('.MP4'):  # Add more video file extensions if needed
                    video_path = os.path.join(root, video_file)
                    total_frames = get_total_frames(video_path)
                    if total_frames is not None:
                        label = extract_label_from_path(video_path)
                        video_path = video_path.split(os.path.join(project_dir, ""))[-1] #add current computer path, -1 is end of sring array
                        f.write(f"{video_path} {total_frames} {label}\n")

current_path = os.getcwd()
project_directory = os.path.dirname(current_path)
data_directory = current_path + "\\" + r"mmaction2\DataSet\Data"
output_annotation_file = r"mmaction2\DataSet\annotation.txt"
create_annotation_file(data_directory, project_directory, output_annotation_file)


