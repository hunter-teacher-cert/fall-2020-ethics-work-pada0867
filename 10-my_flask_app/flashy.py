from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash

USER = 'abc'
PASS = '123'

#response codes
SUCCESS = 1
BAD_PASS = -1
BAD_USER = -2

flashy = Flask(__name__)
flashy.secret_key = 'ESTOY ES NO SECURO'


def authenticate(user,passwd):
    """ return code indicating login result"""
    if user == USER:
        if passwd == PASS:
            return SUCCESS
        else:
            return BAD_PASS
    else:
        return BAD_USER


@flashy.route('/')
def root():
    if 'user' not in session:
        return render_template( 'form.html', title='Login' )
    else:
        return redirect( url_for('welcome') )


@flashy.route('/auth', methods=['POST'])
def auth():
    print("authing................")
    u = request.form['input_user']
    p = request.form['input_pw']

    print(u)
    print(p)

    result = authenticate(u,p)

    if result == SUCCESS:
        session['user'] = u
        #flash( 'successful is you!' )
        return redirect( url_for('welcome') )
    if result == BAD_PASS:
        print('bad pass')
        flash( 'the pass is bad' )
    elif result == BAD_USER:
        print('bad user, bad!')
        flash( 'the user is bad' )
    return redirect( url_for('root') )


@flashy.route('/welcome')
def welcome():
    if 'user' not in session:
        return redirect( url_for('root') )
    else:
        return render_template( 'home.html',
                                user=session['user'],
                                title='welcome, fam' )


@flashy.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect( url_for('root') )


if __name__ == '__main__':
    flashy.debug = True
    flashy.run()

@flashy.route('/home')
def Home():
    title = "Welcome"
    return render_template('home.html',title = title)

'''
@flashy.route('/larger_font')
def Home_larger_font():
    return redirect( url_for('Home_larger_font') )
'''
@flashy.route('/home_larger_font')
def Home_larger_font():
    title = "Welcome"
    return render_template('home_larger_font.html',title = title)
'''
@flashy.route('/home_smaller_font')
def Home_smaller_font():
    return redirect( url_for('home') )
'''

@flashy.route('/Jack')
def Jack():
    name = 'Jack Padalino'
    title = "Our team: Jack Padalino"
    about_me = 'Hi! My name is {} and I teach Computer Science. I am also taking classes at Hunter College to learn how to be a better CS teacher.'.format(name)
    return render_template('Jack.html', name = name, title = title, about_me = about_me)

@flashy.route('/Huan')
def Huan():
    name = 'Huan Wang'
    title = "Our team: Huan Wang"
    about_me = 'Hi! My name is {} and I teach Computer Science. I am also taking classes at Hunter College to learn how to be a better CS teacher.'.format(name)
    return render_template('Huan.html',name = name, title = title, about_me = about_me)

@flashy.route('/about')
def About():
    title = "About us"
    return render_template('about.html', title = title)
