from flask import render_template, request, redirect, url_for, Response
from app import tracert
from app import database
import platform
import subprocess
import re

def index():
    if request.method == 'POST':
        host = request.form['host']
        if host:
            return redirect(url_for('tracert_progress', host=host))
    return render_template('index.html')

def tracert_progress(host):
    def generate():
        command = ['traceroute', host] if platform.system() != 'Windows' else ['tracert', host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        hops = []
        for line in iter(process.stdout.readline, ''):
            yield f"data:{line.strip()}\n\n"  # Gửi dữ liệu theo thời gian thực tới trình duyệt
            if re.match(r'^\s*\d+', line):
                hop_info = re.split(r'\s{2,}', line.strip())
                if len(hop_info) > 2:
                    hop_number = hop_info[0]
                    ip_address = hop_info[-1]
                    response_times = hop_info[1:-1]
                    hops.append((hop_number, ip_address, response_times))

        process.stdout.close()
        process.wait()
        database.save_to_db(host, hops)

    return Response(generate(), mimetype='text/event-stream')

def results():
    host = request.args.get('host')
    results = database.get_tracert_results(host)
    return render_template('results.html', host=host, results=results)

def saved_results():
    hosts = database.get_all_hosts()
    return render_template('saved_results.html', hosts=hosts)