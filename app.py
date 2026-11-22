from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>GitHub Actions CI/CD</h1>
    <h2>Deployment Successful!</h2>
    <p>Application deployed using AWS ECS and Docker.</p>
    """

@app.route("/health")
def health():
    return {"status": "Healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)