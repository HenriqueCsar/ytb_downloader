function download(){
    var convert = document.getElementById("gender3").value  
    var url_video = document.getElementById("url").value  
    eel.download_video(url_video, convert)()  
}