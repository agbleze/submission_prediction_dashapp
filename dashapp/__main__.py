from dashapp.app import app


if __name__ == '__main__':
    app.run(port=8666, debug=False, use_reloader=False)