// O JavaScript aqui pode ser usado para exibir o status de download, mas o comportamento principal já ocorre no Flask
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();
    const url = document.querySelector('#url').value;
    document.getElementById('status').innerText = "Baixando áudio...";

    fetch('/baixar', {
        method: 'POST',
        body: new URLSearchParams({
            'url': url
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('status').innerText = data;
    })
    .catch(error => {
        document.getElementById('status').innerText = "Erro ao tentar baixar o áudio.";
    });
});
