import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29267685"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9aea863501d41261e6c75ad565b6e1e1")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://patelprinci920:8Wx2qbAgb0kFxOlj@cluster0.8iy9m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
