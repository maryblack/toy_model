from flask import Flask, request, jsonify, make_response
import pickle
# import sklearn
app = Flask(__name__)
clf = pickle.load(open('iris_model.pckl', 'rb'))

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username

@app.route('/api/classify',  methods=['POST', "OPTIONS"])
def predict():
    if request.method=='OPTIONS':
        return _build_cors_prelight_response()
    values = request.get_json()
    answer = int(clf.predict([values['params']])[0])
    print('clf')
    result = {'class': answer}
    resp = make_response(jsonify(result))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()
