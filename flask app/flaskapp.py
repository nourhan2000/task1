from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db=SQLAlchemy(app)


class Users(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    def __repr__(self) -> str:
        return '<name %r>' %self.name 
    

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        user_content = request.form['content']
        new_user= Users(name = user_content)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return "can't add user"

    else:
        users= Users.query.order_by(Users.id).all()
        return render_template('index.html', users=users)


@app.route('/del/<int:id>')
def delete(id):
    user2del= Users.query.get_or_404(id)

    try:
        db.session.delete(user2del)
        db.session.commit()
        return redirect('/')
    except:
            return "can't delete user"

@app.route('/updt/<int:id>', methods=['GET','POST'])
def updat(id):
    user= Users.query.get_or_404(id)
    if request.method=="POST":
        user.name=request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "can't update name"
    else:
        return render_template('updt.html', User=user)

if __name__=="__main__":
    app.run(debug=True)