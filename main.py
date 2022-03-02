import pytube
import datetime, eel

eel.init("view")

@eel.expose
def download_video(url):
    url_video = pytube.YouTube(url)
    video = url_video.streams.first()
    video.download('./Downloads')


# duracao_video = url_video.length
# duracao_video_formatada = datetime.timedelta(seconds=duracao_video)
# print(f"O vídeo dura {duracao_video_formatada}")

# data_publicacao = url_video.publish_date
# print(f"O vídeo foi postado {data_publicacao}")

eel.start("index.html")