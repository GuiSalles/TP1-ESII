from flask import Flask
from database_manager import criar_tabela

app = Flask(__name__)
criar_tabela()

from views import *

if __name__ == "__main__":
    app.run(debug = true)
