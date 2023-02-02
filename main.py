import http.client
import os
import time
import sys

def download_file(url: str):
    # Parse the URL and extract the domain and path
    domain = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:])
    # Connect to the server
    conn = http.client.HTTPSConnection(domain)
    conn.request('GET', path)
    # Get the response and save it to a file
    resp = conn.getresponse()
    filename = os.path.basename(url)
    file = open(filename, 'wb')
    size = 0
    while True:
        # Download the file in chunks and display the size every second
        chunk = resp.read(1024)
        size += len(chunk)
        file.write(chunk)
        time.sleep(1)
        print(f'{size} bytes received')
        if not chunk:
            break
    file.close()
    conn.close()
    # Confirm that the download is complete
    return 'Download complete'


if __name__ == '__main__':
    # Get the URL from the command line argument
    url:str = sys.argv[1]
    print(download_file(url))