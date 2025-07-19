import psycopg2
import socket
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== Supabase Connection Test ===")

# Test different hostname variations
hosts_to_test = [
    "db.tvwaibppahlodxdwswoe.supabase.co",
    "tvwaibppahlodxdwswoe.supabase.co", 
    "db.tvwaibppahlodxdwswoe.supabase.co",
]

for host in hosts_to_test:
    print(f"\n--- Testing {host} ---")
    
    # Test DNS resolution
    try:
        ip = socket.gethostbyname(host)
        print(f"✅ DNS Resolution: {host} -> {ip}")
        
        # Test port connectivity
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((ip, 5432))
        if result == 0:
            print(f"✅ Port 5432 is open")
        else:
            print(f"❌ Port 5432 is closed (error code: {result})")
        sock.close()
        
    except socket.gaierror as e:
        print(f"❌ DNS Resolution failed: {e}")

print(f"\n=== Current Environment Variables ===")
print(f"DB_HOST: {os.environ.get('DB_HOST', 'NOT SET')}")
print(f"DB_PORT: {os.environ.get('DB_PORT', 'NOT SET')}")
print(f"DB_NAME: {os.environ.get('DB_NAME', 'NOT SET')}")
print(f"DB_USER: {os.environ.get('DB_USER', 'NOT SET')}")
print(f"DB_PASSWORD: {'SET' if os.environ.get('DB_PASSWORD') else 'NOT SET'}")

print(f"\n=== Testing Direct Connection ===")
try:
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db.tvwaibppahlodxdwswoe.supabase.co'),
        database=os.environ.get('DB_NAME', 'postgres'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD'),
        port=os.environ.get('DB_PORT', '5432'),
        sslmode='require',
        connect_timeout=10
    )
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    print(f"Error type: {type(e).__name__}") 