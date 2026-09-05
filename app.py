from flask import Flask
app =Flask(__name__)
 
@app.route("/")
def home():
    return "DevSecOps güvenli web uygulaması"
                                                   
if __name__== "__main__":
     app.run(host="0.0.0.0", port=5000)
 eval("1 + 1")

