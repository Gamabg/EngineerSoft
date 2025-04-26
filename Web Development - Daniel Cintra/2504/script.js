// // Array literal (forma mais comum)

// console.log("Array de tarefas:", tarefas);

// // Usando o construtor Array
// const categorias = new Array["Trabalho", "Estudo", "Pessoal", "Projetos"];
// console.log("Array de categorias:", categorias);

// // Array.of (ES6)
// const prioridades = Array.of("Baixa", "Média", "Alta");
// console.log("Array de prioridades:", prioridades);

// // Array.from (ES6) - cria array a partir de uma string
// const letras = Array.from("TaskMaster");
// console.log("Array de letras:", letras);


// // Acesso por índice
// console.log("Primeira tarefa:", tarefas[0]);
// console.log("Última tarefa:", tarefas[tarefas.length - 1]);

// // Modificando um elemento
// tarefas[2] = "Preparar apresentação sobre Arrays";
// console.log("Após modificação:", tarefas);

// // Métodos para adicionar e remover elementos
// tarefas.push("Testar aplicação");    // Adiciona no final
// console.log("Após push:", tarefas);

// const removido = tarefas.pop();         // Remove o último
// console.log("Removido com pop:", removido);
// console.log("Após pop:", tarefas);

// tarefas.unshift("Planejar sprint");      // Adiciona no início
// console.log("Após unshift:", tarefas);

// const removidoInicio = tarefas.shift();  // Remove o primeiro
// console.log("Removido com shift:", removidoInicio);
// console.log("Após shift:", tarefas);

// tarefas.splice(1, 1, "abc")
// console.log(tarefas)


// const tarefas = [
//   "Estudar JavaScript",
//   "Criar projeto TaskMaster",
//   "Preparar apresentação",
//   "Revisar código"
// ];

// tarefas.forEach = (elemento, indice) =>
//   {
//     console.log(`${indice + 1}. ${elemento}`)
//   }

// console.log(tarefas)

// const arrayNovo = tarefas.map((elemento, indice) =>
// {
//   return elemento + "-Concluido"
// })

// console.log(arrayNovo)

// const tarefasComA = tarefas.filter(elemento => elemento.toLowerCase().includes("p"))

// console.log(tarefasComA)

// const tarefaEncontrada = tarefas.find(elemento => elemento.includes("js"))

// console.log(tarefaEncontrada)

// const IndextarefaEncontrada = tarefas.findIndex(elemento => elemento.includes("js"))

// console.log(IndextarefaEncontrada)

// tarefas.splice(IndextarefaEncontrada, 1)

// console.log(IndextarefaEncontrada)

// console.log(tarefas)

// const valorFinal = tarefas.reduce((total, t, indice) => total + indice, 0)

// console.log(valorFinal) 

// const tarefa = {
//   id: 1,
//   titulo: "Aprender sobre objetos",
//   descricao: "Estudar propriedades e metodos",
//   concluida: false,
//   prioridade: "alta",
//   dataCriação: new Date()
// }

// console.log(tarefa)

// console.log(tarefa?.titulo)
// console.log(tarefa['titulo'])

// const tarefasEspeciais = {
//   "data-criação": new Date(),
//   "nome da tarefa":"nome da tarefa separado"
// }

// console.log(tarefasEspeciais["nome da tarefa"])


//     this.tarefas.push(novaTarefa);
//     console.log(`Tarefa "${titulo}" adicionada.`);
//     return novaTarefa;
//   },
//   listarTarefas() {
//     console.log(`Projeto ${this.nome} - Lista de Tarefas:`);
//     this.tarefas.forEach(t => console.log(`- ${t.id}: ${t.titulo} (${t.prioridade})`));
//   }
// };

// projetoTaskMaster.adicionarTarefa("Estudar Objetos", "alta");
// projetoTaskMaster.adicionarTarefa("Criar interface");
// projetoTaskMaster.listarTarefas();

// Object.values


// const prioridades = ["baixa", "media", "alta"]

// // const baixa = prioriadade [0]
// // const media = prioriadade [1]
// // const alta = prioriadade [2]

// const [baixa, media, alta] = prioridades 

// console.log(baixa, media, alta)

// const categorias = ["trabalho", "estudo", "pessoal", "saude"]

//  console.log(categorias)

//  const [primeraCategoria, ... outrasCategorias] = categorias

// console.log
// (primeraCategoria, outrasCategorias)


const projetoTaskMaster = {
     nome: "TaskMaster",
     version: "1.0",
     autor: "Curso JavaScript",
     tarefas: [],
     
  };
  
const {nome, version, ... outrasProps} = projetoTaskMaster

console.log|(nome)
console.log(version)
console.log(outrasProps)



