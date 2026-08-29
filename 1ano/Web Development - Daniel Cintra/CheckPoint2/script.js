// Exc 1 
console.log("Exc 1")
let tarefaConcluida = true;  

if (tarefaConcluida === true) {
  console.log("A tarefa está concluída!");
} else {
  console.log("A tarefa não foi concluída.");
}

// Exc 2
console.log("Exc 2")
let prioridade = 2; 

if (prioridade === 1) {
    console.log("Prioridade Baixa");
} else if (prioridade === 2) {
    console.log("Prioridade Média");
} else if (prioridade === 3) {
    console.log("Prioridade Alta");
} else {
    console.log("Prioridade Inválida");
}

//Exc 3 
console.log("Exc 3")
let diaSemana = new Date().getDay(); 

switch (diaSemana) {
    case 0:
        console.log("Domingo");
        break;
    case 1:
        console.log("Segunda-feira");
        break;
    case 2:
        console.log("Terça-feira");
        break;
    case 3:
        console.log("Quarta-feira");
        break;
    case 4:
        console.log("Quinta-feira");
        break;
    case 5:
        console.log("Sexta-feira");
        break;
    case 6:
        console.log("Sábado");
        break;
    default:
        console.log("Dia inválido");
}

// Exc 4
console.log("Exc 4")
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// Exc 5
console.log("Exc 5")
let soma = 0; 
let i = 1;    

while (i <= 5) {
    soma += i; 
    i++;
}

console.log("A soma total é: " + soma);

// Exc 6
console.log("Exc 6")
let contador = 3; 

do {
    console.log(contador); 
    contador--;            
} while (contador > 0);   

console.log("FIM!"); 

// Exc 7
console.log("Exc 7")
function verificarIdade(idade) {
    if (idade < 18) {
        return "Menor de idade";
    } else if (idade >= 18 && idade < 60) {
        return "Maior de idade";
    } else {
        return "Idoso";
    }
}

console.log(verificarIdade(15)); 
console.log(verificarIdade(25)); 
console.log(verificarIdade(60));

// Exc 8 
console.log("Exc 8")
let temSenhaCorreta = true; 
let temBiometriaAutenticada = false; 

let acessoPermitido = temSenhaCorreta || temBiometriaAutenticada;

console.log("Acesso Permitido:", acessoPermitido);
console.log("Acesso Negado:", !acessoPermitido);

// Exc 9
console.log("Exc 9")
let tarefas = "Estudar, Fazer exercícios, Ler um livro, Preparar o jantar";

let arrayTarefas = tarefas.split(", ");

let tarefasFormatadas = arrayTarefas.join(" | ");

let temEstudar = arrayTarefas.includes("Estudar");

console.log("Array de Tarefas:", arrayTarefas);
console.log("Tarefas Formatadas:", tarefasFormatadas);
console.log("Contém 'Estudar':", temEstudar);

// Exc 10
console.log("Exc 10")

function gerarNumeroAleatorio() {
    return Math.floor(Math.random() * (15 - 5 + 1)) + 5;
}
let raio = gerarNumeroAleatorio();
console.log("Raio do Círculo:", raio);


function calcularAreaCirculo(raio) {
    return (Math.PI * Math.pow(raio, 2)).toFixed(2);
}
let area = calcularAreaCirculo(raio);
console.log("Área do Círculo:", area);

