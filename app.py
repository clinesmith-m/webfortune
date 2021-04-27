from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os
import subprocess

app = Flask("fortune_app")
app.secret_key = b'REPLACED_ME_x#pi*CO0@^z'

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    fortune_out = subprocess.check_output(["fortune"]).decode()
    web_out = "<pre>" + fortune_out + "</pre>"
    return web_out

@app.route('/cowsay/<message>/')
def cowsay_vanilla(message):
    arg_list = ["cowsay"] + message.split()
    cow_out = subprocess.check_output(arg_list).decode()
    web_out = "<pre>" + cow_out + "</pre>"
    return web_out

@app.route('/cowfortune/')
def cowsay_piped():
    fortune_out = subprocess.check_output(["fortune"]).decode()
    cow_args = ["cowsay"] + fortune_out.split()
    cow_out = subprocess.check_output(cow_args).decode()
    web_out = "<pre>" + cow_out + "</pre>"
    return web_out
