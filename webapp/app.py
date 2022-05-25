from bumbo.api import API
from storage import BookStorage
from auth import STATIC_TOKEN


app = API()
book_storage = BookStorage()
book_storage.create(name="7 habits of highly effective people", author="Stephen Covey")

@app.route("/login", allowed_methods=["post"])
def login(req, resp):
    resp.json = {"token": STATIC_TOKEN}


@app.route("/", allowed_methods=["get"])
def index(req, resp):
    books = book_storage.all()
    resp.html = app.template("index.html", context={"books": books})
