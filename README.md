🎵 YouTube Audio Downloader

Este é um aplicativo web simples feito com Flask que permite baixar áudio de vídeos do YouTube usando yt-dlp.

🚀 Funcionalidades
✅ Baixa apenas o áudio dos vídeos do YouTube
✅ Interface web simples e intuitiva
✅ Suporte a diferentes formatos de áudio
✅ Download direto para a pasta downloads/

🎯 Pré-requisitos
Antes de rodar o projeto, certifique-se de ter instalado:

Python 3.3+
pip (gerenciador de pacotes do Python)

🔧 Instalação e Execução

1️⃣ Clone o repositório
git clone https://github.com/luanribeiro7/ytb-audio
cd ytb-audio

2️⃣ Instale as dependências
pip install -r requirements.txt

3️⃣ Execute a aplicação
python app.py

4️⃣ Acesse no navegador
Abra: http://127.0.0.1:5000/

🏗 Estrutura do Projeto

📂 ytb audio
│── 📂 static  
│   ├── 📂 css  
│   │   ├── styles.css  
│   ├── 📂 js  
│   │   ├── script.js  
│── 📂 templates  
│   ├── index.html  
│── 📂 downloads  (pasta onde os arquivos baixados serão salvos)  
│── app.py  
│── requirements.txt  
│── README.md  
│── .gitignore  
📂 yt_dlp_folder (backend Python)

📌 Tecnologias Utilizadas
Flask → Framework web em Python
yt-dlp → Biblioteca para baixar vídeos/áudios do YouTube
HTML + CSS + JavaScript → Interface web
Python - Backend 

📌 Feito por Luan Ribeiro
