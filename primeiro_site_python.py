from flask import Flask,render_template


app = Flask(__name__)
#Criação de estrutura padrão do Flask para criação de site

#Para cada página é necessário criar:
# - Route = o caminho após o diminio
# - Função =  o que se quer exibir naquela página

#Decorate = Função responsável por atribuir uma nova funcionalidade uma função
#Def = definição
@app.route ("/")
def home ():
    return render_template("homepage.html")

#criando mais uma página
@app.route ("/contatos")
def contatos():
    return render_template ("contatos.html")

@app.route ("/usuarios/<nome_usuario>")#Deixando o nome do usuário dinamico colocando o (/<>) isso informa para o Flask o q vire após a barra será oq está dentro de (<>)
def usuarios(nome_usuario): #Faz com que o nome do usuário seja usado como parametro
    return render_template("usuarios.html", nome_usuario=nome_usuario)


if __name__ == "__main__": #execução do código somente quando o arquivo foir executado diretamente por este arquivo
    # Colocar site no Ar
    # debug=true = ativar a debugação do site
    app.run(debug=True)



















