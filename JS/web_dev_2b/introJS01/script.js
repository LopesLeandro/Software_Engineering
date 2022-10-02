//alert("Socorooooooooo!")
//Comentário de linha 
/*Comentário de bloco*/
/*
let salario = 20000; //Existe diferença entre let e var
var idade = 99;

let resposta = confirm("Você está certo disso, posso perguntar?");
console.log(resposta);

let resp = prompt("Informe sua data de nascimento", "dd/mm/aaaa");
console.log(resp);*/

window.document.write("Agora eu acredito!");
document.write("Pior que é verdade.");

//TIPO NUMBER
a = 10;
console.log(a + " " + typeof(a));

a = 20.5;
console.log(a + " " + typeof(a));

//TIPO LÓGICO
a = true;
console.log(a + " " + typeof(a));

//TIPO STRING
a = "Como assim isso é uma variável";
console.log(a + " " + typeof(a));

//ARRAY
a = ['Posição 1','Posição 2'];
console.log(a[0] + " " + typeof(a));
a[0] = "outra coisa"
console.log(a[0] + " " + typeof(a));

//ARRAY DINÂMICO
a = new Array();
a[0] = "outra outra coisa";
console.log(a + " " + typeof(a));

//OBJETO
a = new Object();
a.idade = 10;
console.log(a.idade + " " + typeof(a));

//DECLARAÇÃO DE UMA FUNÇÃO
function botao1(){
    let nome = window.document.getElementById("txtnome").value;
    alert('O botão foi clicado ' + nome + ' seu querido.');
}

console.log('ANTES')
botao1();
console.log('DEPOIS')

//OPERADORES LÓGICOS

//IGUALDADE
let x = 43;
console.log(x == 43);
console.log(x == "43");
console.log(x == 67);
console.log(x == "67");

//IDENTIDADE
console.log(x === 43);
console.log(x === "43");

