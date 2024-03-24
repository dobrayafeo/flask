from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True)
