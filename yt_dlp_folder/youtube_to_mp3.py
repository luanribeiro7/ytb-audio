import yt_dlp
import os

def baixar_audio_youtube(url, pasta_saida=""):
    try:
        print(f"Iniciando o download do URL: {url}")
        
        if not pasta_saida:
            pasta_saida = os.getcwd()  # Diretório atual

        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(pasta_saida, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando: {url}")
            info = ydl.extract_info(url, download=True)

        # Exibe informações sobre o arquivo baixado
        print(f"Download concluído: {info['title']}.{info['ext']}")
        
        # Retorna o nome do arquivo com extensão
        return f"{info['title']}.{info['ext']}"
    
    except Exception as e:
        print(f"Erro ao baixar o áudio: {e}")
        return None