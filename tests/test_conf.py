def test_app(app):
    assert app.config['ENV'] == "test"
    assert app.config['DEBUG']
    assert app.config['TESTING']
