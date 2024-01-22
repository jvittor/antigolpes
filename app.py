from flask import Flask, render_template, request, jsonify
from pysafebrowsing import SafeBrowsing

app = Flask(__name__)
s = SafeBrowsing('AIzaSyCuEVNiq9Zc-ccKbHeuw7q1xjAasEfDczA')  # Substitua 'YOUR_API_KEY' pela sua chave de API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.get_json()
    url = data.get('url')

    try:
        result = s.lookup_urls([url])

        if result and url in result:
            details = result[url]
            return jsonify({
                'url': url,
                'malicious': details['malicious'],
                'platforms': details['platforms'],
                'threats': details['threats']
            })
        else:
            return jsonify({'error': 'Não foi possível obter informações para o site.'})

    except Exception as e:
        return jsonify({'error': f"Erro ao verificar o site: {e}"})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from pysafebrowsing import SafeBrowsing

app = Flask(__name__)
s = SafeBrowsing('AIzaSyCuEVNiq9Zc-ccKbHeuw7q1xjAasEfDczA')  # Substitua 'YOUR_API_KEY' pela sua chave de API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.get_json()
    url = data.get('url')

    try:
        result = s.lookup_urls([url])

        if result and url in result:
            details = result[url]
            return jsonify({
                'url': url,
                'malicious': details['malicious'],
                'platforms': details['platforms'],
                'threats': details['threats']
            })
        else:
            return jsonify({'error': 'Não foi possível obter informações para o site.'})

    except Exception as e:
        return jsonify({'error': f"Erro ao verificar o site: {e}"})


if __name__ == '__main__':
    app.run(debug=True)
