from flask import Flask
from config import Config
import sys
sys.path.append("../GraduateWorkFormatter")
#from GraduateWorkFormatter import formatter

app = Flask(__name__)
app.config.from_object(Config)
# os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)

from app import routes