from flask import Flask, render_template


app = Flask(__name__)

# Rota para meu index
@app.route('/')
def home():
    return render_template("index.html")

# Rota para Artesanato
@app.route('/artesanato')
def artesanato():
    # Vai procurar 'artesanato/artesanato.html' dentro da pasta 'templates'
    return render_template('artesanato/artesanato.html')


# Rota para Comidas
@app.route('/comidas')
def comidas():
    # Vai procurar 'comidas/comidas.html' dentro da pasta 'templates'
    return render_template('comidas/comidas.html')

# Rota para Música (Você não tem essa pasta na imagem, mas o link existe)
@app.route('/musica')
def musica():
    return render_template('musica/musica.html') 

# Rota para Cultura Digital
@app.route('/cultura_digital')
def cultura_digital():
    # Vai procurar 'cultura/cultura-digital.html' dentro da pasta 'templates'
    return render_template('cultura/cultura-digital.html')


if __name__ == '__main__':
    app.run(debug=True)
