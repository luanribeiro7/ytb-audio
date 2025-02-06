document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    const urlInput = document.getElementById("url").value;
    const loading = document.getElementById("loading");
    const resultDiv = document.getElementById("result");

    // Exibir o loading
    loading.style.display = "block";
    resultDiv.textContent = "";  // Limpa o resultado anterior

    fetch("/baixar", {
        method: "POST",
        body: new URLSearchParams({
            url: urlInput
        })
    })
    .then(response => response.text())
    .then(html => {
        document.body.innerHTML = html;  // Atualiza a página com a resposta
        loading.style.display = "none";   // Esconde o loading
    });
});
