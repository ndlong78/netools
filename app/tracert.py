import subprocess
import re
import platform

def tracert_host(host):
    command = ['traceroute', host] if platform.system() != 'Windows' else ['tracert', host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    hops = []
    for line in iter(process.stdout.readline, ''):
        print(line.strip())  # Hiển thị tiến trình theo thời gian thực
        if re.match(r'^\s*\d+', line):
            hop_info = re.split(r'\s{2,}', line.strip())
            if len(hop_info) > 2:
                hop_number = hop_info[0]
                ip_address = hop_info[-1]
                response_times = hop_info[1:-1]
                hops.append((hop_number, ip_address, response_times))

    process.stdout.close()
    process.wait()
    return hops