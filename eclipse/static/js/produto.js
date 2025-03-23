//variaveis
const quantia = document.getElementById("quantia");
const quantia_options = 10

//adicionando opções a quantia
for (let index = 1; index <= quantia_options; index++) {
    const element = document.createElement('option');
    element.value = index;
    element.textContent = index;
    quantia.appendChild(element);
}