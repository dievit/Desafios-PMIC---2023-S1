function verificar_eventos() {
    var respostas = document.querySelectorAll('input[type="radio"]:checked');
    var corretas = ['c', 'c', 'a', 'b', 'a', 'c', 'd', 'd'];
    var acertos = 0;
    for (var i = 0; i < respostas.length; i++) {
        if (respostas[i].value === corretas[i]) {
            acertos++;
        }
    }
    var resultado = document.getElementById('resultado');
    resultado.innerHTML = "Você acertou " + acertos + " de " + corretas.length + " questões.";
}