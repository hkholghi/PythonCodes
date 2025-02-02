
from google.colab import drive
drive.mount('/content/drive')

# Install necessary libraries
!pip install --upgrade google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account JSON key file
SERVICE_ACCOUNT_FILE = '/content/drive/My Drive/Colab Notebooks/service_account_key.json'

# Scopes required for Admin SDK
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

# Authenticate with the service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Impersonate a super admin user
delegated_credentials = credentials.with_subject('hkholghi@abingtonfriends.net')

# Build the Admin SDK service
service = build('admin', 'directory_v1', credentials=delegated_credentials)

# Retrieve a list of users in the domain
results = service.users().list(customer='my_customer', maxResults=25).execute()
users = results.get('users', [])

# Print user information
if not users:
    print('No users found.')
else:
    print('Users:')
    for user in users:
        print(f"Name: {user['name']['fullName']}, Email: {user['primaryEmail']}")

