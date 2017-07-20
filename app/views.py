from app import app


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {""}
    return 'Its Working! yay!'
