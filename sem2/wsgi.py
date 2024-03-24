from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        mail = session['mail']
        return render_template('index.html', username=username, mail=mail)
    else:
        return redirect(url_for('login'))


@app.route('/shoes/')
def shoes():
    _shoes = [
        {
            "name": "Абаркасы (avarcas)",
            "price": '15 $',
            "description": 'Сандалии, которые придумали испанские крестьяне с острова Менорка. Это летняя обувь '
                           'с закрытым носом и открытой пяткой. Традиционно изготавливается из натуральных материалов.'
                           ' В Россию абаркасы привёз бренд Legitimas.',
        },
        {
            "name": "Аскетичные броги (austerity brogues)",
            "price": '25 $',
            "description": 'классические туфли с W-образными швами на мысах. Главной особенностью аскетичных брогов '
                           'является отсутствие декоративной перфорации (отсюда и название). Модель пришла из мужского'
                           ' гардероба, как и большинство классических вариантов.',
        },
    ]
    return render_template('shoes.html', content=_shoes)


@app.route('/accessories/')
def accessories():
    _accessories = [
        {
            "name": "Ornamentals",
            "price": '17 $',
            "description": 'украшения',
        },
        {
            "name": "Jewelry",
            "price": '15 $',
            "description": 'бижутерия',
        },
        {
            "name": "Jew",
            "price": '10 $',
            "description": 'бижутерия',
        },
    ]
    return render_template('accessories.html', content=_accessories)


@app.get('/login/')
def checker_get():
    return render_template('login.html')


@app.post('/login/')
def login():
    if request.method == 'POST':
        if not request.form['username']:
            flash('Ошибка, забыли ввести имя !', 'danger')
            return redirect(url_for('login'))
        if not request.form['mail']:
            flash('Ошибка, забыли ввести почту !', 'danger')
            return redirect(url_for('login'))
        # session
        session['username'] = escape(request.form.get('username'))
        session['mail'] = escape(request.form.get('mail'))
        # Cookie
        response = make_response(render_template('index.html', username=session['username'], mail=session['mail']))
        response.set_cookie('username', session['username'])
        response.set_cookie('mail', session['mail'])
        return response


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('mail', None)
    print(f'(Exit) username: {request.cookies.get("username")}')
    print(f'mail: {request.cookies.get("mail")}')
    response = make_response(render_template('login.html'))
    response.delete_cookie("username")
    response.delete_cookie("mail")
    # response.set_cookie(*request.cookies, expires=0)
    return response


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
