import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page  # Run the test here

    # Stop tracing and save trace file with test name
    trace_path = f"traces/{request.node.name}_trace.zip"
    context.tracing.stop(path=trace_path)
    context.close()
    print(f"✅ Trace saved: {trace_path}")
