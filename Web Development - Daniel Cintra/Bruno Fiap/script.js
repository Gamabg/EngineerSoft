
/*
console.log("Hello World")
console.info("Info")
console.warn("warning")
console.error("Error")

console.table([
    {id: 1, tarefa: "Estudar JS"},
    {id: 2, tarefa: "Praticar Código"}
])

console.group("Grupo de Logs")
console.log("Log 1")
console.log("Log 2")
console.groupEnd()

console.time("Timer")
//... alguma coisa
if (1 == 2) {
    console.log("não")
}
console.timeEnd("Timer")

//comentario de 1 linha 

/*
comentario de 
varis linhas
*/


/*
var antigo = "valor da variavel"
console.log(antigo)

let variavelMutavel = 1

const variavelImutavel = 2

console.log(variavelImutavel)
*/

//Tipo de dados primitivos

// let texto = "texto"
// console.log(typeof texto)

// let numero = 4
// console.log(typeof numero)

// let IsCompleted = false
// console.log(typeof IsCompleted)

// let semValor 
// console.log(typeof semValor)

// let nulo = null
// console.log(typeof nulo)

// let uniqueId = Symbol("id")
// console.log(typeof uniqueId)

// let bigNumero = 99999999999999n
// console.log(typeof bigNumero)

//Tipos de Dados Avançados

let tarefa = {id: 1, tarefa: "Estudar JS"}
console.log(tarefa)
console.log(tarefa.id)
console.log(tarefa.tarefa)

let tasks = [
   {id: 1, tarefa: "Estudar JS"},
   {id: 2, tarefa: "Praticar Código"}
]

console.log(tasks)
console.log(tasks[0])
console.log(tasks[0]['id'])

let hoje = new Date()
console.log(hoje)

let pattern = /^[a-z]+$/i;
console.log(pattern)