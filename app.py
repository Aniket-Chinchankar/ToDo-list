from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    snp = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.snp} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        new_todo = Todo(title=title, desc=desc)
        try:
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your todo"
    else:
        todos = Todo.query.all()  # Query all Todo items from the database
        return render_template('index.html', todos=todos)  # Pass the todos to the template

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(todo_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that todo"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your todo"
    else:
        return render_template('update.html', todo=todo)

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)