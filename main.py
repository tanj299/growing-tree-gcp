import time
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#Flask configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tree:tree@35.225.107.184/tree'
db = SQLAlchemy(app)

#Timer configuration
Time = True
def timer():
    otherResult = db.engine.execute ("select * from age")
    # python syntax // divides and round down to integer
    result = [row[0]//15 for row in otherResult]
    # mins = 0
    # secs = 60
    # mins_prev = 0

    # while(Time == True):
    #     secs = secs - 1
    #     time.sleep(1)

    #     if(secs == 0):
    #         mins = mins + 1
    #         secs = 60

    #         if(mins > mins_prev):
    #             db.engine.execute("UPDATE age SET frameNum = frameNum + 1")
    #             result = db.engine.execute("select * from age")
    #             print([row[2] for row in result])
    #             mins_prev = mins

    #         otherResult = db.engine.execute("select * from age")
    #         print([row[0] for row in otherResult])
    #         timer()
    # result = result / 15
    return result


@app.route('/')
def root():
    # Fetch the most recent tree frame number.
    times = timer()

    return render_template(
        'index.html', frames=times)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
