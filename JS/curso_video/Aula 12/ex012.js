var agora = new Date()
var hora = agora.getHours()
var minutos = agora.getMinutes()

if (hora >1) {
    console.log(`Agora são ${hora}:${minutos}.`)
} else {
    console.log(`Agora é ${hora}:${minutos}.`)
}
if (hora <5) {
    console.log('Volte a dormir maníaco.')
} else if (hora <12) {
    console.log('Bom dia.')
} else if (hora <18) {
    console.log('Boa tarde.')
} else if (hora >18) {
    console.log('Boa noite.')
}