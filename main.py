from website import create_app

app = create_app()

if __name__ == "__main__": # basically only run this if we ran the 'main.py' file
    app.run(debug=True) # debug = True means reload the website every time we change our python code