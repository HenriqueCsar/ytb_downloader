import pytube
import datetime, eel, subprocess, os, glob

eel.init("view")

@eel.expose
def download_video(url, convert):
    list_of_result = {'duration':'', 'title':''}

    
    url_video = pytube.YouTube(url)
    video = url_video.streams.first()
    video.download('./Downloads')
    local = os.getcwd()
    for i in glob.glob('.//Downloads//*'):
        print(i)
        if(convert):
            subprocess.call(f'{local}//Features//ffmpeg//bin//ffmpeg.exe -i "{i}" "{i}.{convert}"', shell=True)
            os.remove(i)
            subprocess.call(f'"{i}.{convert}"', shell=True)

    #duration of video        
    duracao_video = url_video.length
    duracao_video_formatada = datetime.timedelta(seconds=duracao_video)
    duracao_video_formatada = str(duracao_video_formatada)
    list_of_result['duration'] = duracao_video_formatada


    #title
    titulo_video = url_video.title
    list_of_result['title'] = titulo_video



    subprocess.call('cls', shell=True)
    return list_of_result

                      




# data_publicacao = url_video.publish_date
# print(f"O vídeo foi postado {data_publicacao}")

eel.start("index.html")
