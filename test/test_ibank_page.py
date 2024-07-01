from model.user import User

#@pytest.mark.parametrize()
def test_switch_to_ibank_page(app):
    app.session.switch_to_ibank_page()

def test_select_first_region_on_ibank_page(app):
    app.ibank.open_ibank_page()
    app.ibank.select_first_region()