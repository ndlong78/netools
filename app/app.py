from app import app
import tracert
import database

@app.route('/')
def index():
    host = 'google.com'  # Bạn có thể thay đổi host theo nhu cầu
    tracert_output = tracert.tracert_host(host)
    hops = tracert.parse_tracert(tracert_output)
    database.save_to_db(host, hops)
    results = database.get_tracert_results(host)
    return render_template('index.html', host=host, results=results)

if __name__ == '__main__':
    app.run(debug=True)