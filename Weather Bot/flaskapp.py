from flask import Flask, render_template, request,redirect
import bot

app= Flask(__name__, template_folder='template')

class Conv:
    def __init__(self,msg,reply):
        self.msg= msg
        self.reply=reply

conv=[]

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        msg = request.form['content']
        reply = bot.chat(msg,"localhost")
        covy=Conv(msg,reply)
        conv.append(covy)
        return redirect('/')
       
    else:
        return render_template('index.html', msgs=conv)


if __name__=="__main__":
    app.run(debug=True)