from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    # Fetching form data
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    # Saving the data to a file (You can modify this to save to a database)
    with open("users.txt", "a") as file:
        file.write(f"{name},{email},{password}\n")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
