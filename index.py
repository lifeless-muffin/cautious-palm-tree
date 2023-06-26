# load environment varaibles
from dotenv import load_dotenv
load_dotenv() # configuration

# import servies and modules
from services.database import DatabaseManager


def main():
    
    # example document
    document = {'title': 'russia invades US', 'description': 'Russia is invading US...' }
    client = DatabaseManager.get_client()
    print(client)

if __name__ == '__main__':
    main()