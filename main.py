from sys import argv
from pytube import YouTube


link = argv[1]  # getting the first argument as the link
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Channel: ", yt.author)
print("Date: ", yt.publish_date)

# define the download quality
downloader = yt.streams.get_by_resolution('720p')
# downloader = yt.streams.get_highest_resolution()

# define the download directory
downloader.download("/home/amantha/Downloads/")
