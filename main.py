import pytube
import datetime, eel, subprocess, os, glob
import speech_recognition as sr

eel.init("view")

@eel.expose
def download_video(url, convert):
    list_of_result = {'duration':'', 'title':'', 'thumb':'', 'transcription':''}

    
    url_video = pytube.YouTube(url)
    video = url_video.streams.first()
    
    video.download('./Downloads')
    local = os.getcwd()
    for i in glob.glob('.//Downloads//*'):
        print(i)
        if(convert):
            nome_arquivo = i
            subprocess.call(f'{local}//Features//ffmpeg//bin//ffmpeg.exe -i "{i}" "{i}.{convert}"', shell=True)
            subprocess.call(f'{local}//Features//ffmpeg//bin//ffmpeg.exe -i "{i}" "{i}.wav"', shell=True)
            os.remove(i)        

    #duration of video        
    duracao_video = url_video.length
    duracao_video_formatada = datetime.timedelta(seconds=duracao_video)
    duracao_video_formatada = str(duracao_video_formatada)
    list_of_result['duration'] = duracao_video_formatada


    #title
    titulo_video = url_video.title
    list_of_result['title'] = titulo_video

    # thumb
    thumb_video = url_video.thumbnail_url
    list_of_result['thumb'] = thumb_video


    #transcription
    r = sr.Recognizer()

    with sr.AudioFile(f'{nome_arquivo}.wav') as source:
        audio_data = r.listen(source)
        mensagem = r.recognize_google(audio_data, language="pt-PT", show_all=True)
        mensagem = mensagem['alternative'][0]['transcript']
    
    list_of_result['transcription'] = mensagem
    os.remove(f'{nome_arquivo}.wav')
    
    subprocess.call(f'"{nome_arquivo}.{convert}"', shell=True)

    subprocess.call('cls', shell=True)
    
    return list_of_result



# data_publicacao = url_video.publish_date
# print(f"O vídeo foi postado {data_publicacao}")

eel.start("index.html", size=(1048, 700))
