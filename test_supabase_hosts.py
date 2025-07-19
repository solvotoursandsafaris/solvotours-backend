import socket
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== Testing Supabase Hostname Resolution ===")

# Possible hostname formats
possible_hosts = [
    "db.tvwaibppahlodxdwswoe.supabase.co",
    "tvwaibppahlodxdwswoe.supabase.co",
    "db.tvwaibppahlodxdwswoe.supabase.co",
    "tvwaibppahlodxdwswoe.supabase.co:5432",
]

for host in possible_hosts:
    print(f"\nTesting: {host}")
    try:
        # Try to resolve the hostname
        ip = socket.gethostbyname(host.split(':')[0])  # Remove port if present
        print(f"✅ DNS Resolution: {host} -> {ip}")
        
        # Try to connect to port 5432
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, 5432))
        if result == 0:
            print(f"✅ Port 5432 is open on {host}")
        else:
            print(f"❌ Port 5432 is closed on {host}")
        sock.close()
        
    except socket.gaierror as e:
        print(f"❌ DNS Resolution failed: {e}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")

print("\n=== Checking your current .env settings ===")
print(f"DB_HOST: {os.environ.get('DB_HOST', 'NOT SET')}")
print(f"DB_PORT: {os.environ.get('DB_PORT', 'NOT SET')}") 