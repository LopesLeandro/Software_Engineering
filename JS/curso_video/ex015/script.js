function verificar(){
    //window.alert('Funcionou Animal!')
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById('txtano')
    var res = window.document.querySelector('div#res')
    
        if (fano.value.length == 0 || fano.value > ano) {
            window.alert('ERRO! Verifique os dados e tente novamente seu animal.')

        } else {
            var fsex = window.document.getElementsByName('radsex')
            var idade = ano - Number(fano.value)
            var genero = ''
            var img = document.createElement('img')
                      img.setAttribute('id', 'foto')
            if (fsex[0].checked) {
                    genero = 'Macho'
                    if (idade >= 0 && idade <= 10) {
                        //criança
                        img.setAttribute('src', 'crianca-homem.png')
                    } else if (idade < 15) {
                        //Adolescente
                        img.setAttribute('src', 'adolescente-homem.png')
                    } else if (idade < 21) {
                        //Jovem
                        img.setAttribute('src', 'adulto-homem.png')
                    } else if (idade < 50) {
                        //Adulto
                        img.setAttribute('src', 'adulto-homem.png')
                   } else {
                       //Velho
                        img.setAttribute('src', 'velho-homem.png')
                   }

                } else if (fsex[1].checked) {
                    genero = 'Fêmea'
                    if (idade >= 0 && idade <= 10) {
                        //criança
                        img.setAttribute('src', 'crianca-mulher.png')
                    } else if (idade < 15) {
                        //Adolescente
                        img.setAttribute('src', 'jovem-mulher.png')
                    } else if (idade < 21) {
                        //Jovem
                        img.setAttribute('src', 'jovem-mulher.png')
                    } else if (idade < 50) {
                        //Adulta
                        img.setAttribute('src', 'adulta-mulher.png')
                   } else {
                       //Velha
                       img.setAttribute('src', 'velha-mulher.png')
                   }
                }

            res.style.textAlign = 'center';
            res.innerHTML = `Detectamos que você é ${genero} e sua idade calculada é de ${idade} anos. </br></br>`
            res.appendChild(img) 
        }
}