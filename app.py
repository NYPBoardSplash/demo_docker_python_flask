from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def hello(): 
	return "This is a Hello Beautiful World! moxing9876" 
if __name__ == "__main__": 
	app.run(host="0.0.0.0")
