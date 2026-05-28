from playwright.sync_api import sync_playwright

def extract_gdp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.worldometers.info/gdp/gdp-by-country/")

        rows = page.locator("tr").all()

        final = {}
        for row in rows:
            cells = row.locator("td").all_inner_texts()
            if len(cells) > 0:
                country = cells[1]
                gdp = cells[2]
                gdp_full_value = cells[3]
                gdp_growth = cells[4]
                gdp_per_capital = cells[5]

                final[country] = {
                    "gdp": gdp,
                    "gdp_full_value": gdp_full_value,
                    "gdp_growth": gdp_growth,
                    "gdp_per_capital": gdp_per_capital
                }

        browser.close()
        return final