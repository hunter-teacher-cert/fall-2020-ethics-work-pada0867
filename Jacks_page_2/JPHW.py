from flask import Flask, render_template, request
    
app = Flask(__name__)

@app.route('/')
def home():
    title = "Welcome"
    return render_template('home.html',title = title)

@app.route('/Jack')
def Jack():
    name = 'Jack Padalino'
    title = "Our team: Jack Padalino"
    about_me = 'Hi! My name is {} and I teach Computer Science. I am also taking classes at Hunter College to learn how to be a better CS teacher.'.format(name)
    return render_template('Jack.html', name = name, title = title, about_me = about_me)

@app.route('/Huan')
def Huan():
    name = 'Huan Wang'
    title = "Our team: Huan Wang"
    about_me = 'Hi! My name is {} and I teach Computer Science. I am also taking classes at Hunter College to learn how to be a better CS teacher.'.format(name)
    return render_template('Huan.html',name = name, title = title, about_me = about_me)

@app.route('/About')
def About():
    title = "About us"
    return render_template('About.html', title = title)
