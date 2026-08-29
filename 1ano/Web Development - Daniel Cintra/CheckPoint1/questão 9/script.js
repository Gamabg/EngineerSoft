function compararNumeros(a, b) {
    if (a > b) {
        return "A é maior";
    } else if (b > a) {
        return "B é maior";
    } else {
        return "Ambos são iguais";
    }
}
//ok
console.log(compararNumeros(5, 10));
//ok
console.log(compararNumeros(10, 5));
//ok
console.log(compararNumeros(7, 7));
//ok
