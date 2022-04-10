from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response, Blueprint
from itsdangerous import Signer, BadSignature

apiStudents = Blueprint('apiStudents' , __name__ , url_prefix = '/app/students')

@apiStudents.route('/')
def index() :
    return jsonify({"message" : "Welcome Student Page"})