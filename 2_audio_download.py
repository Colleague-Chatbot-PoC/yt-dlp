import os
import subprocess
import sys
import shutil

def download_audio(video_url, output_dir):
    # Find the path to ffmpeg
    ffmpeg_path = shutil.which("/opt/homebrew/bin/ffmpeg")
    if not ffmpeg_path:
        print("ffmpeg is not found in PATH")
        sys.exit(1)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Download and convert the audio to mp3 using yt-dlp
    try:
        result = subprocess.run([
            'yt-dlp',
            '-x', '--audio-format', 'mp3',
            '--ffmpeg-location', ffmpeg_path,
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
    except FileNotFoundError as e:
        print(f"Error: yt-dlp or ffmpeg not found")
        sys.exit(1)

if __name__ == "__main__":
    # URL of the video to download
    VIDEO_URL = "https://www.youtube.com/watch?v=td1KAgrYUGA"  # Change this to the actual video URL

    # Output directory (optional)
    OUTPUT_DIR = "audio_downloads"

    download_audio(VIDEO_URL, OUTPUT_DIR)