from flask import Flask
from repository.Cliente_Repository import Cliente_Repository
from controller.cliente.ClienteController import ClienteController
app = Flask(__name__)

@app.route("/")
def hello_world():
    return Cliente_Repository.save()

@app.route("/submit_form", methods=["POST"])
def submit_form():
    return ClienteController.create_post()

if __name__ == "__main__":
    app.run(debug=True)

