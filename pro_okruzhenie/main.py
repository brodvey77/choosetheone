import os

import dotenv


dotenv.load_dotenv()

print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))