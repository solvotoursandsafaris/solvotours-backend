import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== Railway Database Connection Test ===")

print(f"DB_HOST: {os.environ.get('DB_HOST', 'metro.proxy.rlwy.net')}")
print(f"DB_PORT: {os.environ.get('DB_PORT', '33691')}")
print(f"DB_NAME: {os.environ.get('DB_NAME', 'railway')}")
print(f"DB_USER: {os.environ.get('DB_USER', 'postgres')}")
print(f"DB_PASSWORD: {'SET' if os.environ.get('DB_PASSWORD') else 'NOT SET'}")

try:
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'metro.proxy.rlwy.net'),
        database=os.environ.get('DB_NAME', 'railway'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD'),
        port=os.environ.get('DB_PORT', '33691'),
        sslmode='require',
        connect_timeout=10
    )
    print("✅ Railway database connection successful!")
    
    # Test a simple query
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ Database version: {version[0]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"❌ Railway database connection failed: {e}")
    print(f"Error type: {type(e).__name__}")
    
    if "password authentication failed" in str(e):
        print("\n💡 This suggests the password is incorrect.")
        print("Please check your Railway database password in the .env file.")
    elif "connection" in str(e).lower():
        print("\n💡 This suggests a network or host issue.")
        print("Please check your Railway database host and port.") 