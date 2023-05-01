from pages.swag_labs import SwagLabs

def test_icon_exist(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.welcomeUser()
    swag_labs_page.welPass()
    assert swag_labs_page.exist_icon()