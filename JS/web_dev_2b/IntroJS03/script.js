function infinity(){
    let i = 0;
    while(i < 50000) {
        console.log(i++) //incremento pós fixado
    }
}

function date(){
    console.log(newDate());
}

infinity();
date();