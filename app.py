from flask import Flask, render_template, url_for, request, redirect
import os
from enyo.enyoencryption import EnyoEncryption
from enyo.enyodecryption import EnyoDecryption

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
app.config['SECRET_KEY'] = 'abc123@567$#'

@app.route('/')
def index():
    return render_template('index.html', result = "CLICK ENCRYPT / DECRYPT")

@app.route('/encrypt',methods=['POST'])
def encrypt():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        partitions = request.form['partitions']
        trans = request.form.getlist('trans') 
        transposition = True
        if(len(trans)==0):
            transposition = False
        try:
            if transposition:
                result = EnyoEncryption(text, key, partition=int(partitions), transposition=transposition).encrypted
            else:
                result = EnyoEncryption(text, key, partition=int(partitions)).encrypted
        except:
            result = "Invalid Partitions"
        return render_template('index.html', result = result)
    
@app.route('/decrypt',methods=['POST'])
def decrypt():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        partitions = request.form['partitions']
        trans = request.form.getlist('trans') 
        transposition = True
        if(len(trans)==0):
            transposition = False
        try:
            if transposition:
                result = EnyoDecryption(text, key, partition=int(partitions), transposition=transposition).decrypted
            else:
                result = EnyoDecryption(text, key, partition=int(partitions)).decrypted
        except:
            result = "Invalid Partitions"
        final = ""
        for i in result:
            if(ord(i)>0):
                final = final + i
        result = final
        return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)