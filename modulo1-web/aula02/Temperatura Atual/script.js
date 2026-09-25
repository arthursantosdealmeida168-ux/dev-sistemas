const cidade = document.getElementById("cidade");
const buscar = document.getElementById("buscar");
const resultado = document.getElementById("resultado");

buscar.addEventListener("click", () => {
    // Pega o nome da cidade selecionada
    const nomeCidade = cidade.options[cidade.selectedIndex].text;

    // Pega latitude e longitude do value do select
    const [lat, lon] = cidade.value.split(",");

    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    resultado.innerHTML = "Consultando clima...";

    fetch(url)
        .then(resposta => {
            if (!resposta.ok) {
                throw new Error("Erro na requisição");
            }

            return resposta.json();
        })
        .then(data => {
            const temperatura = data.current_weather.temperature;

            let fundo;

            if (temperatura < 15) {
                fundo = "linear-gradient(180deg, #2193b0, #6dd5ed)";
            } else if (temperatura < 25) {
                fundo = "linear-gradient(180deg, #74ebd5, #ACB6E5)";
            } else {
                fundo = "linear-gradient(180deg, #ff9966, #ff5e62)";
            }

            document.body.style.background = fundo;

            // Exibe os dados
            resultado.innerHTML = `
                <h2>${nomeCidade}</h2>
                <div style="font-size: 60px;">${icone}</div>
                <p>Temperatura atual: <strong>${temperatura} °C</strong></p>
            `;
        })
        .catch(erro => {
            console.error(erro);

            resultado.innerHTML = `
                <p>Não foi possível consultar os dados do clima.</p>
            `;

            document.body.style.background =
                "linear-gradient(180deg, #555, #222)";
        });
});