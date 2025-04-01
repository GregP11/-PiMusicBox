from flask import Flask, request
import subprocess
import threading

app = Flask(__name__)

def play_music(url):
    output_file = "/tmp/music.mp3"
    subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", output_file, url])
    subprocess.run(["mpv", output_file])

@app.route('/play', methods=['POST'])
def receive_url():
    data = request.json
    url = data.get('url')
    if url:
        threading.Thread(target=play_music, args=(url,)).start()
        return 'Lecture en cours', 200
    else:
        return 'URL manquante', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
