import pytube
import datetime

url = input("Url do youtube: ")

url_video = pytube.YouTube(url)

video = url_video.streams.first()

#aumentar a resolução
#video = url_video.streams.get_highest_resolution()

video.download()


duracao_video = url_video.length
duracao_video_formatada = datetime.timedelta(seconds=duracao_video)
print(f"O vídeo dura {duracao_video_formatada}")

data_publicacao = url_video.publish_date
print(f"O vídeo foi postado {data_publicacao}")

