# Configuration for the Federated Learning Powerline Detection

# Database settings
database = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database_name': 'your_database'
}

# Model paths
model_paths = {
    'local': '/path/to/local/model',
    'remote': '/path/to/remote/model'
}

# Server configuration
server = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': True
}