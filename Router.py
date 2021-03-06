from flask import redirect, send_from_directory

class Router:
  def __init__(self, app, processing):
    @app.route("/api/dependencies")
    def send_dependencies():
        return processing.get_tree()

    @app.route("/api/security")
    def send_security():
        return "{}"

    @app.route("/api/statistic")
    def send_statistic():
        return processing.get_by_frequency()

    @app.route("/")
    def index():
        return redirect("/index.html")

    @app.route("/<path:path>")
    def send_client(path):
        return send_from_directory('client', path)