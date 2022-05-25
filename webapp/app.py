from bumbo.api import API

app = API()

@app.route("/", allowed_methods=["get"])
def index(req, resp):
    resp.html = app.template("index.html")
