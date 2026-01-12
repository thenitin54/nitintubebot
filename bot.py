<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YouTube Video & MP3 Downloader</title>

<meta name="description" content="Free YouTube Video & MP3 Downloader. Fast, simple, no login required.">
<meta name="robots" content="index, follow">

<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:Arial, Helvetica, sans-serif;
}

body{
  min-height:100vh;
  background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
  display:flex;
  justify-content:center;
  align-items:center;
  color:#fff;
}

.container{
  width:100%;
  max-width:420px;
  padding:20px;
}

.card{
  background:rgba(255,255,255,0.08);
  backdrop-filter:blur(15px);
  border-radius:18px;
  padding:24px;
  box-shadow:0 0 40px rgba(0,0,0,.6);
  text-align:center;
}

h1{
  font-size:26px;
  margin-bottom:6px;
}

.subtitle{
  font-size:14px;
  opacity:.85;
  margin-bottom:18px;
}

input, select{
  width:100%;
  padding:14px;
  margin-bottom:12px;
  border:none;
  border-radius:12px;
  outline:none;
  font-size:14px;
}

button{
  width:100%;
  padding:14px;
  border:none;
  border-radius:14px;
  background:linear-gradient(90deg,#ff416c,#ff4b2b);
  color:#fff;
  font-size:16px;
  font-weight:bold;
  cursor:pointer;
  box-shadow:0 0 18px rgba(255,65,108,.6);
}

button:hover{
  opacity:.9;
}

.note{
  font-size:12px;
  opacity:.7;
  margin-top:14px;
}

.social-title{
  margin-top:20px;
  font-size:14px;
  opacity:.9;
}

.social{
  display:flex;
  justify-content:space-around;
  margin-top:10px;
}

.social img{
  width:42px;
  filter:drop-shadow(0 0 6px rgba(255,255,255,.7));
}

.footer{
  margin-top:18px;
  font-size:12px;
  opacity:.75;
}
</style>
</head>

<body>

<div class="container">
  <div class="card">

    <h1>🎬 YouTube Downloader</h1>
    <div class="subtitle">Video • MP3 • Fast • Free • No Login</div>

    <input id="videoUrl" type="text" placeholder="Paste YouTube video link here">

    <select id="type">
      <option value="video">🎥 Video (MP4)</option>
      <option value="audio">🎵 Audio (MP3)</option>
    </select>

    <button onclick="download()"> Download</button>

    <div class="note">
      ⚠️ This tool supports YouTube videos only.<br>
      We do not host any media.
    </div>

    <div class="social-title">Follow me on</div>

    <div class="social">
      <a href="https://www.youtube.com/@thenitin93" target="_blank">
        <img src="https://img.icons8.com/color/96/youtube-play.png" alt="YouTube">
      </a>

      <a href="https://www.instagram.com/the_nitin_54" target="_blank">
        <img src="https://img.icons8.com/color/96/instagram-new.png" alt="Instagram">
      </a>

      <a href="https://t.me/the_nitin_54" target="_blank">
        <img src="https://img.icons8.com/color/96/telegram-app.png" alt="Telegram">
      </a>

      <a href="https://pinterest.com/kushwanshinitin" target="_blank">
        <img src="https://img.icons8.com/color/96/pinterest.png" alt="Pinterest">
      </a>
    </div>

    <div class="footer">
      RAN  ❤️  BY    NITIN 
    </div>

  </div>
</div>

<script>
function download(){
  const url = document.getElementById("videoUrl").value.trim();
  const type = document.getElementById("type").value;

  if(!url){
    alert("Please paste a YouTube link");
    return;
  }

  if(!url.includes("youtube.com") && !url.includes("youtu.be")){
    alert("Only YouTube links are supported");
    return;
  }

  const format = type === "audio" ? "mp3" : "mp4";

  const downloadURL =
    "https://loader.to/api/button/?url=" +
    encodeURIComponent(url) +
    "&f=" + format;

  window.open(downloadURL, "_blank");
}
</script>

</body>
</html>
