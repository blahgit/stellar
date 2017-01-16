#!/usr/bin/python

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, make_response, Response
import sys
import os.path

import urllib2
import json
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	d=dict()
	if request.method == "GET":
		return render_template('home.html')
	if request.method=="POST":
		result=""
		if request.form.get("addr", ""):
			addr=request.form["addr"]
			try:
				res=urllib2.urlopen("https://horizon-testnet.stellar.org/accounts/%s" %(addr)).read()
			except Exception as e:
				 return render_template('home.html')
			d=json.loads(res)
			d["balance"]=d["balances"][0]["balance"]
		return render_template('home.html', results=d, keys=["account_id", "sequence", "id", "balance"])

if __name__ == "__main__":
    app.secret_key = os.urandom(56457)
    app.run(debug=True,host='0.0.0.0', port=34234)
