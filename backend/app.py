from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if __name__=='main_':
    app.run(debug=True,port=os.getenv('PORT'))