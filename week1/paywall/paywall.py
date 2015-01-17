from flask import Flask
from flask import request, redirect, url_for, render_template, jsonify
from block_io import BlockIo

app = Flask(__name__)


block_io = BlockIo('22fc-4d6f-1f78-e7ce', 'blockchainudemo1', 2)
CONTENT_PRICE = 0.009



@app.route('/')
def hello_world():
    token = request.args.get('token', None)
    if not token:
        return redirect(url_for('token'))

    balance_res = block_io.get_address_balance(labels=token)
    if balance_res["status"] != "success":
        print "ERROR getting balance; cannot verify token"
        return render_template("error.html")

    balance = float(balance_res["data"]["available_balance"])
    if balance >= CONTENT_PRICE:
        return render_template('content.html')
    else:
        return redirect(url_for('token', insufficient=True))

@app.route('/get_address')
def get_token():
    address = block_io.get_new_address()
    return jsonify(**address)

@app.route('/get_balance')
def get_balance():
    balance_res = block_io.get_address_balance(addresses=request.args.get('address', None))
    return jsonify(**balance_res)




@app.route('/token')
def token():
    return render_template('token.html', content_price=CONTENT_PRICE,
                           insufficient=request.args.get('insufficient', False))


if __name__ == '__main__':
    app.run()
