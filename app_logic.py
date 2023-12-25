import pytube
from pytube import YouTube
import os 

class YouTubeDownloader:

    @classmethod 
    def download_video(self, url):

        # url = input("VIDEO URL : ")
        
        youtubeObject = YouTube(url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        
        path = os.path.expanduser('~user')
        
        try:
            youtubeObject.download(path)
            print("Video succesfully downloaded.")
        except:
            print("An error has occurred.")
            
    
if __name__ == "__main__":
    # YouTubeDownloader.main()
    print("please import to use.")
