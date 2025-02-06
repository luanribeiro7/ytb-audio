from flask import Flask, render_template, request
import yt_dlp as youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/baixar', methods=['POST'])
def baixar_audio():
    url = request.form['url']
    try:
        # Opções para baixar apenas o áudio
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,  # Baixar apenas áudio
            'audioquality': 1,  # Melhor qualidade
            'outtmpl': 'downloads/%(id)s.%(ext)s',  # Defina o nome do arquivo de saída
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "Áudio baixado com sucesso!"
    except Exception as e:
        return f"Erro ao baixar áudio: {e}"

if __name__ == '__main__':
    app.run(debug=True)