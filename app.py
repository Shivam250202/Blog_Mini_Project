from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:%40Shivam2502@localhost:3306/blog_platform'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Create tables in the database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/admin')
def admin():
    posts = Post.query.all()
    return render_template('admin.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    if title and content:
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return jsonify({"message": "Post created successfully"})

    return jsonify({"error": "Missing 'title' or 'content' parameter"}), 400

@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post:
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
