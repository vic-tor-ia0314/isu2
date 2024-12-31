from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    data = request.json
    function = data.get('function', 'x**2')
    
    try:
        x = np.linspace(-10, 10, 500)
        y = eval(function)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label=f"y = {function}")
    plt.title("Graph Calculator")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(alpha=0.3)
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close()

    return jsonify({'plot': f"data:image/png;base64,{plot_data}"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
