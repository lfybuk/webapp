from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML-шаблон для простого фронта
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Веб Приложение</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
        .container { width: 80%; margin: auto; padding: 20px; }
        h1 { text-align: center; }
        pre { background-color: #fff; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Тестовое Веб Приложение</h1>
        <h2>GET запрос</h2>
        <form action="/get" method="get">
            <input type="text" name="param1" placeholder="Параметр 1">
            <input type="text" name="param2" placeholder="Параметр 2">
            <button type="submit">Отправить</button>
        </form>
        
        <h2>POST запрос</h2>
        <form action="/post" method="post">
            <input type="text" name="param1" placeholder="Параметр 1">
            <input type="text" name="param2" placeholder="Параметр 2">
            <button type="submit">Отправить</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/get', methods=['GET'])
def get_route():
    params = request.args.to_dict()
    return jsonify(params)

@app.route('/post', methods=['POST'])
def post_route():
    params = request.form.to_dict()
    return jsonify(params)

@app.route('/head', methods=['HEAD'])
def head_route():
    return '', 200

@app.route('/options', methods=['OPTIONS'])
def options_route():
    return '', 200

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error="Метод не поддерживается"), 405

if __name__ == '__main__':
    app.run(debug=True)

