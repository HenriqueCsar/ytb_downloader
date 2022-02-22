from pytube import YouTube
import datetime

url_video = YouTube("https://www.youtube.com/watch?v=WuiY_f0NUzE")

descricao = url_video.description
print(descricao)

duracao_video = url_video.length
duracao_video_formatada = datetime.timedelta(seconds=duracao_video)
print(f"O vídeo dura {duracao_video_formatada}")

data_publicacao = url_video.publish_date
print(f"O vídeo foi postado {data_publicacao}")

