from flask import Flask, render_template, url_for, request, redirect
from model import predict
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__,template_folder='template')


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']

		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)

	
		caption = predict("static/"+img.filename)
		result_dic = {
			
			'description' : caption
		}
        

	return render_template('index.html', results = result_dic)

allowed_extensions = ['jpg', 'png', 'pdf']

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions

@app.route('/', methods = ['POST'])
def upload_pdf():
    
    if request.method == 'POST':
        
        pdf = request.files['pdf']
        pdf.save("static/"+pdf.filename)
        caption = extract("static/"+pdf.filename)
        result_dic = {
            
            'description' : caption}
    return render_template('index.html', results = result_dic)


if __name__ == '__main__':
	app.run(debug = True,use_debugger=False, use_reloader=False)