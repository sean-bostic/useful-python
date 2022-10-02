from pytube import YouTube
from typer import Typer

app = Typer()

@app.command()
def download_vid(url: str, output: str = "./"):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()


if __name__ == "__main__":
    app()
