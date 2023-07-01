from flask import Flask, render_template, request, jsonify
import sys
from io import StringIO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run', methods=['POST'])
def run_code():
    code = request.form.get('code')
    try:
        # Capture output
        old_stdout = sys.stdout
        sys.stdout = output_buffer = StringIO()

        exec(code)

        sys.stdout = old_stdout
        output = output_buffer.getvalue()
        return jsonify({'status': 'success', 'output': str(output)})
    except Exception as e:
        return jsonify({'status': 'error', 'output': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
