def test_app(app):
    assert app.config['ENV'] == "test"
    assert app.config['DEBUG'] == True
    assert app.config['TESTING'] == True
