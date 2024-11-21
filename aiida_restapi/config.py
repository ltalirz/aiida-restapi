"""Configuration of API"""

from importlib.metadata import version

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    'johndoe@example.com': {
        'pk': 23,
        'first_name': 'John',
        'last_name': 'Doe',
        'institution': 'EPFL',
        'email': 'johndoe@example.com',
        'hashed_password': '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW',
        'disabled': False,
    }
}

# The chunks size for streaming data for download
DOWNLOAD_CHUNK_SIZE = 1024

API_CONFIG = {
    'PREFIX': version('aiida_restapi'),  # prefix for all URLs
    'VERSION': '0.1.0a',
}
