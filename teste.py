from flask import Flask, request, jsonify
import requests  

app = Flask(__name__)

@app.route('/buscar_contrato', methods=['POST'])
def buscar_contrato():
    nome_cliente = request.json.get('nome')
    
    if not nome_cliente:
        return jsonify({"erro": "Nome não fornecido"}), 400
    
   
    contrato_url = f"https://api.contratos.com/{nome_cliente}.pdf"  
    
    return jsonify({"contrato_url": contrato_url})

if __name__ == '_main_':
    app.run(debug=True, host="0.0.0.0", port=5000)
