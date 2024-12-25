import subprocess
import re
import platform

def tracert_host(host):
    # Sử dụng 'traceroute' trên Linux và 'tracert' trên Windows
    command = ['traceroute', host] if platform.system() != 'Windows' else ['tracert', host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output

def parse_tracert(output):
    hops = []
    lines = output.split('\n')
    for line in lines:
        if re.match(r'^\s*\d+', line):
            hop_info = re.split(r'\s{2,}', line.strip())
            if len(hop_info) > 2:
                hop_number = hop_info[0]
                ip_address = hop_info[-1]
                response_times = hop_info[1:-1]
                hops.append((hop_number, ip_address, response_times))
    return hops