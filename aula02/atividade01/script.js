const nomeJogador = "Roberto";
let idade = 22;
let online = true;

let jogoFavorito = {
    nome: "Pokémon emerald",
    anoLancamento: 2004
};

let pontuacoes = [100, 76, 40];

console.log("Nome:", nomeJogador, "Tipo:", typeof nomeJogador);
console.log("Idade:", idade, "tipo:", typeof idade);
console.log("Online:", online, "Tipo:", typeof online);
console.log("Jogo Favorito:", jogoFavorito, "Tipo:", typeof jogoFavorito);
console.log("Pontuações:", pontuacoes, "Tipo:", typeof pontuacoes);

idade = 18;
online = false;
console.log("Idade:", idade, "tipo:", typeof idade);
console.log("Online:", online, "Tipo:", typeof online);

//nomeJogador = "Outro nome";
//console.log("Nome:", nomeJogador, "Tipo:", typeof nomeJogador);
//Não alterar constantes

// Desafio extra: calcular a média das 3 pontuações
let soma = pontuacoes[0] + pontuacoes[1] +pontuacoes[2];
let media = soma / pontuacoes.length;
console.log("A média de pontos do jogador " + nomeJogador + " foi: " + media.toFixed(2));