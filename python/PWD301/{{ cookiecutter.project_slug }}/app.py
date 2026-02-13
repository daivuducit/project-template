import os
from app import create_app
from config import get_config

config_name = os.environ.get('FLASK_ENV', 'development')
config = get_config(config_name)

app = create_app(config)

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Flask application...")
    print(f"Environment: {config_name}")
    print(f"Debug mode: {debug}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"URL: http://{host}:{port}")
    
    app.run(host=host, port=port, debug=debug)