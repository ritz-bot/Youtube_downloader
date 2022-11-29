from pytube import YouTube
def Download(link):
  youtubeObject=YouTube(link)
  youtubeObejct=youtubeObject.streams.get_highest_resolution()

try:
  youtubeObject.Download()
except:
  print("There was an error in downloading the video")
print("This download was successful")

link=input("please enter the url: ")
Download(link)
