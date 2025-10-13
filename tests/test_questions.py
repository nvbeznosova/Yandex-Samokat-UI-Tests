import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("index", list(range(8)))
def test_each_question_opens_answer(driver, index):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.scroll_to_questions()
    home.click_question_by_index(index)
    answer_text = home.get_answer_text_by_index(index)
    assert answer_text.strip() != ""