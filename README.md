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

---

## 🔧 Installation — Étapes complètes

### 1. Cloner le dépôt
```bash
git clone https://github.com/TON_UTILISATEUR/PiMusicBox.git
cd PiMusicBox
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances Python
```bash
pip install flask yt-dlp requests
```

### 4. Installer `mpv` (lecteur audio)
```bash
sudo apt update
sudo apt install mpv
```

### 5. Créer les dossiers nécessaires (automatique à l'exécution)
```bash
mkdir -p /tmp/uploads
mkdir -p ~/musics
```

---

## 🔄 Alternative : Installation avec `pipx`

### Installer pipx (si ce n’est pas déjà fait)
```bash
sudo apt install pipx
pipx ensurepath
```

### Installer les outils CLI isolés avec pipx
```bash
pipx install yt-dlp
```

### Utiliser un environnement virtuel local pour Flask (recommandé)
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests
```

> `pipx` est pratique pour les outils CLI comme `yt-dlp`. Pour les scripts personnalisés (comme `app.py` et `receiver.py`), l’usage d’un `venv` local reste recommandé.

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

### 2. Ouvrir un deuxième terminal, puis lancer l’interface web
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

### 4. Utilisation de l’interface
- Coller un lien YouTube pour jouer la musique automatiquement
- Ou envoyer un fichier `.mp3` local pour le lire instantanément
- Le titre s'affiche automatiquement avant l'envoi

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
