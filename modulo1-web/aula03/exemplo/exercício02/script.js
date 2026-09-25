const tituloCard = document.getElementById("tituloCard");
const criarCard = document.getElementById("criarCard");
const cardsContainer = document.getElementById("cardsContainer");

criarCard.addEventListener("click", function () {
    const titulo = tituloCard.value.trim();

    if (titulo === "") {
        alert("Digite um título para o card.");
        return;
    }

    const card = document.createElement("div");

    const h3 = document.createElement("h3");
    h3.textContent = titulo;

    const botaoRemover = document.createElement("button");
    botaoRemover.textContent = "Remover";

    
    botaoRemover.addEventListener("click", function () {
        card.remove();
    });

    card.appendChild(h3);
    card.appendChild(botaoRemover);

    cardsContainer.appendChild(card);

    tituloCard.value = "";
});