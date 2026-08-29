let titulo = "Aprender Java";

let descrição = "Estudar manipulação de string";

console.log(titulo, typeof titulo);
console.log(descrição, typeof descrição);

console.log("Tamanho da variavel Titulo:", titulo.length);
console.log("Tamanho da variavel Descrição:", descrição.length);

console.log("Primeiro caractere do titulo:", titulo[0]);
console.log("Primeiro caractere da descreição:", descrição[0]);

console.log("Primeiro caractere do titulo:", titulo[titulo.length - 1]);

const palavra = "palavra";

console.log("Caractere na posição 3", palavra.charAt(3));

let categoria = "Estudo";
let infoCompleta = "Categoria: " + categoria + "-" + titulo;

console.log(infoCompleta);

let incocompleta2 = `categoria: ${categoria} - ${titulo}`;
console.log(incocompleta2);

let texto1 = "Posição de Javascript";
console.log(texto1.indexOf("Javascript"));
console.log(texto1.includes("Javascript"));
console.log(texto1.startsWith("Posição"));
console.log(texto1.startsWith("Javascript"));

// Função que trunca uma string se ela for maior que um tamanho máximo
const truncarDescricao = (texto, maxLength = 30) => {
  if (texto.length <= maxLength) {
    return texto;
  }
  return texto.substring(0, maxLength) + "...";
};

let descricaoLonga =
  "Este é um exemplo de uma descrição muito longa que precisará ser truncada para exibição.";
console.log("Descrição truncada:", truncarDescricao(descricaoLonga));
console.log(
  "Descrição truncada (20 caracteres):",
  truncarDescricao(descricaoLonga, 20)
);

let texto = "javascript,programação,web,frotend";

console.log("Texto Original:" ,texto);

console.log("Texto slice:", texto.slice(0, 10));

console.log("Texto Substring:" ,texto.substring(0, 10));

let arrayTags = texto.split(",")


console.table(arrayTags)

console.log(arrayTags.join(","))

// Função para destacar um termo em um texto
const destacarTermo = (texto, termo) => {
  if (!termo) return texto;
  const regex = new RegExp(termo, 'gi');
  return texto.replace(regex, `**$&**`);
}

let busca = destacarTermo("JavaScript é uma linguagem incrível. Amo javascript!", "javascript");
console.log("Resultado com destaque:", busca);

// Exibindo constantes
console.log("Math.PI:", Math.PI);
console.log("Math.E:", Math.E);

// Cálculo da área de um círculo
const raio = 5;
const areaCirculo = Math.PI * Math.pow(raio, 2);
console.log(`Área de um círculo com raio ${raio}: ${areaCirculo}`);

//Arredondamento
const numero = 9.7;
console.log("Math.round(9.7):", Math.round(numero));
console.log("Math.floor(9.7):", Math.floor(numero));
console.log("Math.ceil(9.7):", Math.ceil(numero));
console.log("Math.trunc(9.7):", Math.trunc(numero));

const pi = Math.PI;
console.log("Pi com 2 casas decimais:", pi.toFixed(2));


// Função para gerar número aleatório entre min e max
const numeroAleatorioEntre = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log("Número aleatório entre 1 e 10:", numeroAleatorioEntre(1, 10));


// Data atual
const hoje = new Date();
console.log("Data atual:", hoje.toString());

// Data a partir de string ISO
const dataISO = new Date("2025-06-15T10:30:00");
console.log("Data a partir de string ISO:", dataISO);

// Data a partir de componentes (mês: 0 a 11)
const dataComponentes = new Date(2025, 5, 15, 10, 30, 0);
console.log("Data a partir de componentes:", dataComponentes);

const hoje2 = new Date()

const formatarData = (data) => {
  const dia = data.getDate()
  const mes = (data,getMonth() +1)
  const ano = data.getFullYear()
  
return `${dia}/${mes}/${ano}`

}

console.log(hoje2.getDate())
console.log(hoje2.getMonth())
console.log(hoje2.getFullYear())


const adcDias = (data, dias) => {
  const novaData = new Date(data)
  novaData.setDate(data.getDate() + dias)

  return novaData
}

console.log(adcDias(hoje2,3))
console.log(adcDias(hoje2,10))
console.log(adcDias(hoje2,30))
console.log(adcDias(hoje2,365))

const dataFinal = new Date ("09-11-2025")

const diferencaMs = dataFinal - hoje2

console.log(diferencaMs)

const diferencaDias = Math.ceil(diferencaMs / (1000 * 60 * 60 * 24))

console.log("Diferença de dias:", diferencaDias)
