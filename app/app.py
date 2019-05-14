#!/usr/bin/env/python3

from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/version")   
def index():
    return ("Version 0.0.2")

@app.route("/")   
def main():
    return ("Main page !")

@app.route("/cpu/", methods=['GET'])
def show_cpu():
    return jsonify(
            {'CPUs statistics' : psutil.cpu_stats()},
        )

    # cpu = [
    #     {'CPUs count:' : psutil.cpu_count()},
    #     {'CPUs statistics' : psutil.cpu_stats()},
    #     {'CPUs times' : psutil.cpu_times()},
    #     {'CPUs frequencys' : psutil.cpu_freq()}
    # ]
    # return jsonify(cpu)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '4000')