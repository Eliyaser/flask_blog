from flask import Flask,render_template,request



app = Flask(__name__)






@app.route("/")
@app.route("/form")
def index():
    return render_template("form.html")



@app.route('/conform', methods=['GET','POST'])
def register():
	if request.method =='POST':
		fget=request.form.get

		n=fget('name')
		a=fget('age')
		c=fget('city')
	return render_template("conform.html",name=n,age=a,city=c)

	



