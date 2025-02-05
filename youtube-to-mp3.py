import yt_dlp
import os

def baixar_audio_youtube(url, pasta_saida=/Users/luancaue/Musica/Youtube Music):
    try:
        # Criar pasta de saída se não existir
        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)

        # Configurar o yt-dlp para baixar apenas o áudio
        ydl_opts = {
            'format': 'bestaudio/best',  # Melhor qualidade de áudio
            'outtmpl': os.path.join(pasta_saida, '%(title)s.%(ext)s'),  # Padrão de saída
        }

        # Baixar o áudio do vídeo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando: {url}")
            ydl.download([url])

        print("Download concluído.")
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    url_video = input("Cole o link do YouTube: ")
    baixar_audio_youtube(url_video)
