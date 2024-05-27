import os
import shutil

# Find the path to ffmpeg
ffmpeg_path = shutil.which("ffmpeg")

if ffmpeg_path:
    print(f"ffmpeg is located at: {ffmpeg_path}")
else:
    print("ffmpeg is not found in PATH")