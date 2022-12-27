#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pubchem/<pubchem_id>")
def pubchem(pubchem_id):
    return render_template("pubchem.html", pubchem_id=pubchem_id)


@app.route("/pdb/<pdb_id>")
def pdb(pdb_id):
    return render_template("pdb.html", pdb_id=pdb_id)


@app.route("/xyz_renderer/")
def xyz_renderer():
    return render_template("xyz_renderer.html")


if __name__ == "__main__":
    app.run()
