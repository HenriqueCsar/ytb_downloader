function download(){  
    var convert = document.getElementById("gender3").value
    var url_video = document.getElementById("url").value  
    eel.download_video(url_video, convert)(results)  
}  

async function results(list_of_result){
    document.getElementById("duration").innerHTML = 'Duração: '+list_of_result['duration']
    document.getElementById("nome_do_video").innerHTML = list_of_result['title']
}  