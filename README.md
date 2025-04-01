### PiMusicBox 🎶

**Un projet Raspberry Pi pour envoyer et écouter automatiquement de la musique depuis YouTube ou des fichiers audio locaux via une interface web simple.**

---

## 🚀 Fonctionnalités

- 🎵 Lecture automatique de liens YouTube (audio uniquement)
- 📂 Envoi de fichiers audio locaux (.mp3) depuis l’interface
- 📝 Historique des musiques lues (titre + lien)
- 🌐 Interface web accessible depuis n’importe quel appareil
- 🔎 Affichage en temps réel du titre de la vidéo YouTube

---

## 🖥️ Pré-requis

- Un Raspberry Pi (ou tout système Linux)
- Python 3
- `yt-dlp`, `mpv`, `flask`, `requests`, `werkzeug`

### Installation des dépendances :
```bash
sudo apt install mpv
pip install flask yt-dlp requests
```

---

## 📁 Arborescence du projet

```
PiMusicBox/
├── app.py               # Interface web (émetteur)
├── receiver.py          # Serveur qui lit la musique (récepteur)
├── history.txt          # Historique des musiques jouées
├── templates/
│   └── index.html       # Page HTML avec formulaire
└── /tmp/uploads/        # Dossier temporaire pour les fichiers locaux
```

---

## 🧪 Utilisation

### 1. Lancer le serveur récepteur
```bash
python3 receiver.py
```

### 2. Lancer l’interface web
```bash
python3 app.py
```

### 3. Accéder à l’interface
Dans un navigateur :
```
http://localhost:8080
```
Ou depuis un autre appareil :
```
http://IP_DU_PI:8080
```

---

## 💡 Idées d’amélioration
- Authentification pour un usage à distance
- Lecture en streaming sans téléchargement
- Ajout d’une playlist locale ou partagée
- Interface mobile améliorée

---

## 📜 Licence
MIT - libre à utiliser, modifier, partager ✨

---

Développé avec ❤️ pour s'amuser avec le son et le code sur Raspberry Pi.

> Tu peux contribuer, améliorer et partager !
