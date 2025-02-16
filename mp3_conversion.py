import subprocess

# Check if yt-dlp is installed
try:
    import yt_dlp
except ImportError:
    # If not installed, install it using pip
    subprocess.run(['pip', 'install', 'yt-dlp'])


import yt_dlp

URLS = [input("URL Link: ")]

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)