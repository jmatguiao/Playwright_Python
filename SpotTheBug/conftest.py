import pytest
import os

# Import the pytest_html plugin API to add extra info (like screenshots)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')  # <-- get pytest-html plugin
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}.png"
            destination = os.path.join(screenshots_dir, file_name)

            page.screenshot(path=destination)

            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.png(destination))
            else:
                rep.extra = [pytest_html.extras.png(destination)]
