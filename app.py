from flask import Flask, render_template, request, redirect, flash
import requests

app = Flask(__name__)
app.secret_key = 'supersecret'

RECEIVER_IP = "127.0.0.1"  # Si tout est sur le même Pi
RECEIVER_PORT = 5000

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        if youtube_url:
            try:
                response = requests.post(
                    f"http://{RECEIVER_IP}:{RECEIVER_PORT}/play",
                    json={"url": youtube_url}
                )
                if response.status_code == 200:
                    flash("Musique envoyée avec succès 🎵")
                else:
                    flash(f"Erreur côté récepteur : {response.text}")
            except Exception as e:
                flash(f"Erreur de connexion : {e}")
        else:
            flash("Merci de coller un lien YouTube.")
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
