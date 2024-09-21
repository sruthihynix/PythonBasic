import pytube
# link = "https://www.youtube.com/watch?v=MbX2nkWufes"
# link="https://youtu.be/cKq06euxQ20"  #variable link =link of the youtube video  ti be downloaded
link=input("Enter the url of the video : ")
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()

print('Video  downloaded....')