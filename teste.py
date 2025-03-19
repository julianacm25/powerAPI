from flask import Flask, request, jsonify
import requests  # Se você precisar fazer outra requisição para um banco de dados, por exemplo

app = Flask(__name__)

@app.route('/buscar_contrato', methods=['POST'])
def buscar_contrato():
    nome_cliente = request.json.get('nome')
    
    if not nome_cliente:
        return jsonify({"erro": "Nome não fornecido"}), 400
    
    # Aqui você chama a API ou faz a lógica para buscar o contrato
    contrato_url = f"https://api.contratos.com/{nome_cliente}.pdf"  # Exemplo
    
    return jsonify({"contrato_url": contrato_url})

if __name__ == '_main_':
    app.run(debug=True, host="0.0.0.0", port=5000)
