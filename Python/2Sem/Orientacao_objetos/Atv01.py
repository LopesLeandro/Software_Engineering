def minhafunc():
    pass

class Pessoa:
    def __init__(self): #construtor
        self.idade = 0
    def responderIdade(self):
        print("minha idade e ", self.idade)
'''
public class Pessoa{
    public int idade;
    public Pessoa(){
        this.idade = 0;
    }
    public void responderIdade(){
        System.out.println("minha idade e " + this.idade)
    }
    public static void main(String args[]){
        Pessoa zezinho = new Pessoa();
        zezinho.idade = 22;
        zezinho.responderIdade()
    }
}
'''
zezinho = Pessoa()
zezinho.idade = 22
zezinho.responderIdade()

mariazinha = Pessoa()
mariazinha.idade = 25
mariazinha.responderIdade()