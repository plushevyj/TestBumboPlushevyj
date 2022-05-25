from bumbo.api import API

from auth import login_required, TokenMiddleware, STATIC_TOKEN
from storage import BookStorage


app = API()
book_storage = BookStorage()
book_storage.create(name="7 habits of highly effective people", author="Stephen Covey")
app.add_middleware(TokenMiddleware)



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


@app.route("/books", allowed_methods=["post"])
@login_required
def create_book(req, resp):
    book = book_storage.create(**req.POST)

    resp.status_code = 201
    resp.json = book._asdict()
