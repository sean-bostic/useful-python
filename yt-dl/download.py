from urllib.error import HTTPError
from pytube import YouTube
from typer import Typer
import shutil

app = Typer()

@app.command()
def download_vid(url: str, output: str = "./vids"):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    try:
        stream.download()
    except HTTPError as e:
        print(f"An error occurred: {e} ")

if __name__ == "__main__":
    app()
