from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Пример данных о товарах
products = [
    {
        'name': 'Ботинки 1',
        'sizes': ['36', '37', '38', '39', '40'],
        'price': 3000,
        'gender': 'женские',
        'image': 'https://fireboxstore.ru/goodsimg/00000025866/~11.jpg__small__.jpg'  # Замените на реальный URL
    },
    {
        'name': 'Ботинки 2',
        'sizes': ['36', '37', '38', '39', '40'],
        'price': 3500,
        'gender': 'мужские',
        'image': 'https://fireboxstore.ru/goodsimg/00000025867/~11.jpg__small__.jpg'  # Замените на реальный URL
    },
    {
        'name': 'Ботинки 3',
        'sizes': ['36', '37', '38', '39', '40'],
        'price': 4500,
        'gender': 'женские',
        'image': 'https://fireboxstore.ru/goodsimg/00000024361/~11.jpg__small__.jpg'  # Замените на реальный URL
    },
    {
        'name': 'Ботинки 4',
        'sizes': ['36', '37', '38', '39', '40'],
        'price': 6000,
        'gender': 'мужские',
        'image': 'https://fireboxstore.ru/goodsimg/00000024271/~11.jpg__small__.jpg'  # Замените на реальный URL
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
