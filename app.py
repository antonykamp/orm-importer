from flask import Flask, request, render_template, url_for

from orm_planpro_converter.converter import ORMConverter

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html', css_file=url_for('static', filename='pico.min.css'), axios_file=url_for('static', filename='axios.min.js'), modal_file=url_for('static', filename='modal.js'))
    return "<p>Welcome to the ORM - PlanPro Converter</p>"

@app.route("/run")
def run_converter():
    polygon = request.args.get('polygon')
    if not polygon:
        return 'No location specified', 400
    conv = ORMConverter()
    return conv.run(polygon), 200

if __name__ == "__main__":
    app.run(debug=True)