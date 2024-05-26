from flask import Flask, request, render_template
import random

app = Flask(__name__)

lettere = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

risposte_precedenti = {
    'nome': set(),
    'cosa': set(),
    'città': set()
}

def genera_lettera_casuale():
    return random.choice(lettere)

def calcola_punteggio (risposte, lettera):
    punteggio = 0
    for categoria in ['nome','cosa', 'città']:
        risposta = risposte[categoria]
        if risposta and risposta[0].upper() == lettera:
            if risposta not in risposte_precedenti[categoria]:
                risposte_precedenti[categoria].add(risposta)
                punteggio += 15 
            else:
                punteggio += 10
    return punteggio

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lettera = request.form['lettera'].upper()
        nome = request.form['nome']
        cosa = request.form['cosa']
        città = request.form['città']

        risposte = {'nome': nome, 'cosa': cosa, 'città': città}
        punteggio = calcola_punteggio(risposte, lettera)

        return render_template('index.html', punteggio=punteggio, nome=nome, cosa=cosa, città=città, lettera=lettera, risposte=risposte)
    
    lettera = genera_lettera_casuale()
    return render_template('index.html', lettera=lettera)
    
if __name__ == '__main__':
    app.run(debug=True)