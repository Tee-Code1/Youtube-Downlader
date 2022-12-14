import youtube_dl

video_url = input("Enter the URL of the YouTube video you want to download: ")

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([video_url])
    except youtube_dl.utils.DownloadError as e:
        if "HTTP Error 403" in str(e):
            print("Sorry, this video is private and cannot be downloaded.")
        else:
            raise e
