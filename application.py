from flask import Flask, request, render_template, json
import pickle

application = Flask(__name__)


@application.route('/getEmotion')
def getEmotion():
    distance = float(request.args.get('distance', None))
    distance = min([100, 200, 300], key=lambda x: abs(x - distance))
    distance = [100, 200, 300].index(distance) - 1
    angle = float(request.args.get('angle', None))
    emotionDict = pickle.load(open('python/emotions', 'rb'))
    angles = list(emotionDict.keys())
    closest1 = min(angles, key=lambda x: abs(x - angle))
    angles.remove(closest1)
    closest2 = min(angles, key=lambda x: abs(x - angle))

    return json.dumps(emotionDict[closest1][distance]) + " " + json.dumps(emotionDict[closest2][distance])

@application.route('/')
def index():
    return render_template('test.html')

application.secret_key = 'na3928ewafds'

if __name__ == "__main__":
    application.debug = True
    application.run(threaded=True)
