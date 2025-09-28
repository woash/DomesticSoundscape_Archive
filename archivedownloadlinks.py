from playwright.sync_api import sync_playwright, TimeoutError

SEARCH_URL = "https://freesound.org/search/?q=domestic+sounds&page=2"  # change page=

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(SEARCH_URL)
    try:
        page.wait_for_selector('.bw-player[data-mp3]', timeout=15000)
        mp3s = page.eval_on_selector_all(
            '.bw-player[data-mp3]',
            'els => els.map(e => e.getAttribute("data-mp3"))'
        )
        if mp3s:
            with open("mp3_urls2.txt", "w") as f:
                for url in mp3s:
                    print(url)
                    f.write(url + "\n")
        else:
            print("No mp3s found on this page.")
    except TimeoutError:
        print("Timed out waiting for players.")
    finally:
        browser.close()
