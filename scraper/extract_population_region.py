from playwright.sync_api import sync_playwright

def extract_population_and_region():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.worldometers.info/geography/countries-of-the-world/")

        rows = page.locator("tr").all()

        final = {}

        for row in rows:
            cells = row.locator("td").all_inner_texts()

            if len(cells) > 0:
                country = cells[1]
                population = cells[2]
                region = cells[3]

                final[country] = {
                    "population": population,
                    "region": region
                }

        browser.close()

        return final