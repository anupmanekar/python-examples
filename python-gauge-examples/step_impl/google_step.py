from getgauge.python import step
from step_impl.page_objects.page_factory import PageFactory

@step('Search term <term> on google page')
def search_term_on_google(term):
    PageFactory.google_page.visit()
    PageFactory.google_page.search(term)

@step('Verify that first result term is <term>')
def verify_first_result(term):
    RESULT = PageFactory.google_page.get_first_result()
    print('Actual String:%s',RESULT)
    print('Expected String:%s',term)
    assert RESULT == term