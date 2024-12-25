from flask import render_template, request, redirect, url_for
import tracert
import database

def index():
    if request.method == 'POST':
        host = request.form['host']
        if host:
            tracert_output = tracert.tracert_host(host)
            hops = tracert.parse_tracert(tracert_output)
            database.save_to_db(host, hops)
            return redirect(url_for('results', host=host))
    return render_template('index.html')

def results():
    host = request.args.get('host')
    results = database.get_tracert_results(host)
    return render_template('results.html', host=host, results=results)