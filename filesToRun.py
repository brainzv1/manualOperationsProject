import subprocess

# Define the list of Python files you want to run in order
files_to_run = ["createAno.py", "distributeData.py", "extractRawFrames.py", "reorganizeData.py"]

# Loop through the list and run each script sequentially
for script in files_to_run:
    subprocess.run(["python", script], check=True)
#Notice: the extractRawFrames.py file takes a lot of time, especially when all frames are captures.
#In order to make a shorter run time you might want to switch to VideoDataset (config) format and use the mp4 files.