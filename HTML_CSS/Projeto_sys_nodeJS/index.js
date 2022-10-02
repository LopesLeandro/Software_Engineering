const express = require('express')
const { engine } = require('express-handlebars')
const { create } = require('express-handlebars')
const bodyparser = require('body-parser')
const path = require('path')
const { application } = require('express')
const app = express()

//const {a , b , c , d} = [1,2,3,4]
const fakedata = [
    {
        id: 1,
        tarefa: 'Investigação #81',
        descricao: 'Comportamento, gestão e liderança',
        vencimento: '2022-05-01',
        prioridade: 'Alta',
        responsavel: 'Leandro',
        tag: 'Compliance',
        finalizada: 'nao'
    },
    {
        id: 2,
        tarefa: 'Investigação #47',
        descricao: 'Conflito de interesses',
        vencimento: '2021-05-09',
        prioridade: 'Média',
        responsavel: 'Leandro',
        tag: 'Gestão de Seguros',
        finalizada: 'nao'
    },
    {
        id: 3,
        tarefa: 'Investigação #69',
        descricao: 'Fraude',
        vencimento: '2022-09-09',
        prioridade: 'Baixa',
        responsavel: 'Leandro',
        tag: 'Auditoria Interna',
        finalizada: 'sim'
    }
]
/*Configura a engine (motor) do express para utilizar o handlebars*/
app.use(bodyparser.urlencoded({extended: false}))
app.set('view engine','handlebars')
app.engine('handlebars', engine())

create({}).handlebars.registerHelper('checked', function(value, test) {
    if (value == undefined) return '';
    return value==test ? 'checked' : '';
});

/*Disponibiliza acesso para as bibliotecas estaticas do bootstrap e jquery*/
app.use('/css', express.static(path.join(__dirname, 'node_modules/bootstrap/dist/css')))
app.use('/js', express.static(path.join(__dirname, 'node_modules/bootstrap/dist/js')))
app.use('/js', express.static(path.join(__dirname, 'node_modules/jquery/dist')))
app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/home', function(req,res){
    //res.send('Eu acredito')
    res.render('index')
})
app.get('/cliente/novo', function(req,res){
    res.render('cliente/formcliente')
})

app.get('/clientes/alterar/:id', function(req,res){
    let idcliente = req.params['id']
    let umcliente = fakedata.find( o => o.id == idcliente)
    res.render('cliente/formcliente', {cliente: umcliente})
})

app.get('/clientes/delete/:id', function(req,res){
    let umcliente = fakedata.find(o => o.id == req.params['id'])
    let index = fakedata.indexOf(umcliente)
    if (index > -1){
        fakedata.splice(index,1)
    }
    res.render('cliente/clientes',{data: fakedata})
})
app.post('/clientes/save', function(req,res){

    let clienteantigo = fakedata.find( o => o.id == req.body.id)
    if (clienteantigo != undefined){
        /*Alterar*/
        clienteantigo.tarefa = req.body.tarefa
        clienteantigo.descricao = req.body.descricao
        clienteantigo.vencimento = req.body.vencimento
        clienteantigo.prioridade = req.body.prioridade
        clienteantigo.responsavel = req.body.responsavel
        clienteantigo.tag = req.body.tag
        clienteantigo.finalizada = req.body.finalizada
    }else{
        /*Cadastrar novo */
        let maxid = Math.max(...fakedata.map(o => o.id))
        if (maxid == -Infinity) maxid = 0

        let novocliente = {
            tarefa: req.body.tarefa,
            descricao: req.body.descricao,
            vencimento: req.body.vencimento,
            prioridade: req.body.prioridade,
            responsavel: req.body.responsavel,
            tag: req.body.tag,
            finalizada: req.body.finalizada,
            id: maxid + 1
        }
        fakedata.push(novocliente)
    }
    res.redirect('/clientes')
})
app.get('/clientes', function(req,res){
    //res.send('Eu acredito')
    res.render('cliente/clientes', {listaclientes: fakedata})
})
/*Inicialização da aplicação NodeJS + Express*/
app.listen(3000, () =>{
    console.log('Server Online - http://localhost:3000/home')
})
