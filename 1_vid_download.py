import os
import subprocess
import sys

def download_video(video_url, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to ffmpeg binary if not in PATH (optional)
    ffmpeg_path = "ffmpeg"  # Change this if ffmpeg is not in your PATH

    # Download the video using yt-dlp
    try:
        result = subprocess.run([
            'yt-dlp',
            '-o', os.path.join(output_dir, '%(title)s.%(ext)s'),
            video_url
        ], check=True)
        if result.returncode == 0:
            print(f"Download successful: {video_url}")
        else:
            print(f"Download failed with return code: {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # URL of the video to download
    VIDEO_URL = "https://www.youtube.com/watch?v=td1KAgrYUGA"  # Change this to the actual video URL

    # Output directory (optional)
    OUTPUT_DIR = "video_downloads"

    download_video(VIDEO_URL, OUTPUT_DIR)