from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)


@app.route('/predict', methods=["POST"])
def predict():
    try:
        data = request.json
    except Exception as e1: 
        return jsonify({'error': f'request failed : {e1}'})
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({'error': str(e)})
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)