import sqlite3

def save_to_db(host, hops):
    conn = sqlite3.connect('network_results.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tracert_results
                 (host TEXT, hop_number INTEGER, ip_address TEXT, response_times TEXT)''')
    
    for hop in hops:
        hop_number, ip_address, response_times = hop
        response_times_str = ', '.join(response_times)
        c.execute("INSERT INTO tracert_results (host, hop_number, ip_address, response_times) VALUES (?, ?, ?, ?)",
                  (host, hop_number, ip_address, response_times_str))
    
    conn.commit()
    conn.close()

def get_tracert_results(host):
    conn = sqlite3.connect('network_results.db')
    c = conn.cursor()
    c.execute("SELECT hop_number, ip_address, response_times FROM tracert_results WHERE host = ?", (host,))
    results = c.fetchall()
    conn.close()
    return results