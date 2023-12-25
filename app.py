import pytube
from pytube import YouTube

class YouTubeDownloader:

    @classmethod 
    def main(self):

        url = input("VIDEO URL : ")
        
        youtubeObject = YouTube(url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        
        
        try:
            youtubeObject.download()
            print("Video succesfully downloaded.")
        except:
            print("An error has occurred.")
            
    
if __name__ == "__main__":
    YouTubeDownloader.main()