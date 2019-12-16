from flask import Flask
from flask import render_template


# app is an object of the flask class
# flask class takes an argument__name
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',title='sokoni')

@app.route('/products')
def products():
    list_products = ['heels','jordan','rubbers','dresses']
    return render_template('products.html',title='allproducts',products=list_products)


@app.route('/products/shoes')
def shoes():
    return 'shoes page'

# @app.route('/products/shoes/<int:id>')
# def shoes_detail(id):
#    return 'shoes page for id' + str(id)
#

@app.route('/products/shoes/<name>/<int:id>')
def shoes_detail(name,id):
    return 'shoes page for {} with id {}'.format(name,id)


if __name__ == '__main__':
    app.run(port=3000,debug=True)

