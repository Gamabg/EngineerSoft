// console.log(saudar("Daniel"))

// const saudar = function (nome) {
//     return `Ola, ${nome}`
// }

// function exibirTarefa(id = 0 , titulo = "Sem valor", prioridade = "Não definida"){

//     if (!id && !titulo && !prioridade) {
//         console.error("Faltou os valores")
//         return
//     }

//     console.log(`Tarefa ${id}: ${titulo}: (Prioridade: ${prioridade}:)`) // template string

// }

// exibirTarefa(1, "Estudar JS", "alta")





//Função para Calcular Estatisticas
// function calcularEstatisticas(numeros) {
//     let soma = 0;
//     let min = numeros[0];
//     let max = numeros[0];
    
    // Itera pelo array para acumular a soma e atualizar os valores de min e max
//     for (let i = 0; i < numeros.length; i++) {
//       soma += numeros[i]; //5
//       if (numeros[i] < min) {
//         min = numeros[i];
//       }
//       if (numeros[i] > max) {
//         max = numeros[i];
//       }
//     }
    
//     const media = soma / numeros.length;
     
//     const divisao = soma / max

//     // Retorna os resultados em um objeto
//     return { soma, media, min, max, divisao };
//   }
  
//   const resultados = calcularEstatisticas([5, 10, 15, 20, 25]);
//   console.log(resultados);





// Arrow function que retorna a subtração de dois números
// const subtrair = (a, b) => a - b;
// console.log("Subtração:", subtrair(20, 5));



// // Utilizando arrow function para dobrar os elementos de um array
// const numeros = [1, 2, 3, 4, 5];
// const dobrados = numeros.map(n => n * 2);
// console.log("Números dobrados:", dobrados);




// // Demonstração de "this" em função tradicional vs. arrow function
// const contador = {
//     valor: 0,
//     incrementarTradicional: function() {
//       setTimeout(function() {
//         // Neste caso, "this" não se refere ao objeto "contador"
//         console.log("Valor (tradicional):", this.valor);
//       }, 100);
//     },
//     incrementarArrow: function() {
//       setTimeout(() => {
//         // A arrow function preserva o contexto do objeto "contador"
//         this.valor++;
//         console.log("Valor (arrow):", this.valor);
//       }, 100);
//     }
//   };
//   contador.incrementarTradicional();
//   contador.incrementarArrow();



// // IIFE: Função definida e executada imediatamente
// (function() {
//     // Variáveis aqui são locais e não poluem o escopo global
//     const a = 1;
//     const b = 2;
//     console.log("Resultado da IIFE (a + b):", a + b);
//   })();



// // Função que cria um contador privado utilizando closure
// function criarContador() {
//     let contador = 0; // Variável privada
//     return {
//       incrementar: function() {
//         contador++;
//         return contador;
//       },
//       valor: function() {
//         return contador;
//       }
//     };
//   }
  
//   const meuContador = criarContador();
//   console.log("Contador:", meuContador.incrementar()); // 1
//   console.log("Contador:", meuContador.incrementar()); // 2


