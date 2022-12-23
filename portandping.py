# Checks open ports and pings major AWS servers

import subprocess
import socket
import keyboard

def check_ports():
    # Host and port to check for open port
    host = 'google.com'
    port = 80

    # Create a socket and try to connect to the host and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        s.connect((host, port))
        print(f"{host}:{port} is open")
    except socket.error as e:
        print(f"{host}:{port} is closed ({e})")
    finally:
        s.close()

def main():
    # List of AWS servers to ping
    aws_servers = ['ec2.us-east-1.amazonaws.com', 'ec2.us-west-2.amazonaws.com', 'ec2.eu-west-1.amazonaws.com']

    # Ping each server and print the response time
    print("PING RESULTS:")
    for server in aws_servers:
        ping = subprocess.run(['ping', '-c', '3', server], stdout=subprocess.PIPE)
        print(f"{server}: {ping.stdout.decode('utf-8')}")

    # Check for open ports
    check_ports()

    # Wait for numpad 6 to be pressed and rerun the script
    while True:
        if keyboard.is_pressed('numpad 6'):
            main()

main()