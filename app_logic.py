import pytube
from pytube import YouTube

class YouTubeDownloader:

    @classmethod 
    def download_video(self, url):

        # url = input("VIDEO URL : ")
        
        youtubeObject = YouTube(url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        
        
        try:
            youtubeObject.download(r'C:\Users\username\Downloads')
            print("Video succesfully downloaded.")
        except:
            print("An error has occurred.")
            
    
if __name__ == "__main__":
    # YouTubeDownloader.main()
    print("please import to use.")
