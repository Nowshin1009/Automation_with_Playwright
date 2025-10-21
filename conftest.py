import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        yield context
        context.close()
        browser.close()


@pytest.fixture
def page(browser_context, request):
    page = browser_context.new_page()

    
    browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page 

    trace_path = f"traces/{request.node.name}_trace.zip"
    browser_context.tracing.stop(path=trace_path)
    print(f"Trace saved: {trace_path}")

    page.close()
