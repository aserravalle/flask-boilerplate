from flask import *

app = Flask(__name__)

model = joblib.load('model.joblib')

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json(force=True)
        prediction = model.predict(data["x"])
        return jsonify(Input=data["x"], Output=prediction)

if __name__ == '__main__':
    app.run(debug=True)
