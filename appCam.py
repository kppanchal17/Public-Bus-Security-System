# 	PiCam Local Web Server with Flask

from flask import Flask, render_template, Response
import sqlite3




from flask import Flask, render_template, Response
# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
      


       
       
       
       # def init():
        #    conn = sqlite3.connect('picam.db')
        
        #c = conn.cursor()
        #c.execute("INSERT INTO data (image) VALUES (frame)")
    #conn.commit()
        
        
        
        
        
        
        #db=sqlite3.connect(picam.db)
        #cur = db.cursor()
        #cur.execute("INSERT INTO data(image) VALUES(date('frame');"
        #db.commit()
        #db.close() 
               
   


