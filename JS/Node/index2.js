function infinity(){
    let i = 0;
    setInterval(function(){
        console.log(i++);
    }, 3);
}
function date(){
    console.log(new Date());
}
infinity();
date();