const botaoBuscar = document.addEventListener("click", async () => {
    const cep = document.getElementById("cep").value;
    const resultado = document.getElementById("resultado");


    if (cep.length !== 8) {
        resultado.innerHTML = "<p>CEP inválido. Digite um CEP com 8 números.</p>";
        return;
    }

    try {
        const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);

        const dados = await resposta.json();

        if (dados.erro) {
            resultado.innerHTML = "<p>CEP inválido ou não localizado.</p>";
            return;
        }

        resultado.innerHTML = `
            <p><strong>Logradouro:</strong> ${dados.logradouro}</p>
            <p><strong>Bairro:</strong> ${dados.bairro}</p>
            <p><strong>Cidade:</strong> ${dados.localidade}</p>
            <p><strong>UF:</strong> ${dados.uf}</p>
        `;

    } catch (erro) {
        resultado.innerHTML =
            "<p>Não foi possível realizar a consulta.</p>";
    }
});