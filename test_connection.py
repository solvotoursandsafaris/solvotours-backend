import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

print("=== Environment Variables Check ===")
print(f"DB_NAME: {os.environ.get('DB_NAME', 'NOT SET')}")
print(f"DB_USER: {os.environ.get('DB_USER', 'NOT SET')}")
print(f"DB_PASSWORD: {'SET' if os.environ.get('DB_PASSWORD') else 'NOT SET'}")
print(f"DB_HOST: {os.environ.get('DB_HOST', 'NOT SET')}")
print(f"DB_PORT: {os.environ.get('DB_PORT', 'NOT SET')}")

print("\n=== Testing Database Connection ===")

try:
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db.tvwaibppahlodxdwswoe.supabase.co'),
        database=os.environ.get('DB_NAME', 'postgres'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('9RUWELd+V#hazf&'),
        port=os.environ.get('DB_PORT', '5432'),
        connect_timeout=10
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print(f"Error type: {type(e).__name__}") 