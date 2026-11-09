let precoProduto = 24;
let quantidade = 5;

let total = precoProduto * quantidade;
let dobro = total * 2;
let resto = total % 2;

console.log("Total da compra:", total);
console.log("Dobro do total:", dobro);
console.log("Resto da divisão:", resto);

let cupomValido = true;
let freteGratis = false;

let algumBeneficio = cupomValido || freteGratis;
let todososBeneficios = cupomValido && freteGratis;

console.log("Algum benefício (OU):", algumBeneficio);
console.log("Todos os benefícios (E):", todososBeneficios);

// Monstrando na Tela
document.getElementById("preço").innerText = "R$ " + precoProduto;
document.getElementById("quantidade").innerText = "R$ " + quantidade;
document.getElementById("total").innerText = "R$ " + total;
document.getElementById("dobro").innerText = "R$ " + dobro;
document.getElementById("resto").innerText = resto;
document.getElementById("cupom").innerText = cupomValido ? "sim" : "não";
document.getElementById("frete").innerText = freteGratis ? "sim" : "não";
document.getElementById("algum").innerText = algumBeneficio ? "sim" : "não";
document.getElementById("todos").innerText = todososBeneficios ? "sim" : "não";