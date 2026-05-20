def test_ui_page(unauthenticated_page):
    assert unauthenticated_page.title() == "SatoriXR"