from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
	return "Hello, world!"
if  __name__ == "__main__":
	app.run()
#Adding Some Comment
#Added one more comment
#Added comment to mark this issue complete
#Added comment to mark this issue DONE

