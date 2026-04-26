rom flask import Flask, request

app = Flask(__name__)

# Rotas
@app.route('/')
def home():
    return 'bem-vindo à homepage, digite "/tabuada" para começar.'

@app.route('/tabuada', methods=['GET', 'POST'])
def tabuada():
    if request.method == 'POST':
        num = int(request.form.get('numero'))
        html = f'<h3> Tabuada do {num} </h3>'
        for i in range(1, 11):
            html += f'{i} x {num} = {i*num}<br>'
            
        html += '<br><a href="/tabuada">Calcular outra</a>'
        return html
    return """
    <form method="POST">
        Numero: <input type="number" step="1" name="numero" required>
        <button type="submit">Enviar</button>
    </form>
    """


if __name__ == '__main__':
    app.run(debug=True)
