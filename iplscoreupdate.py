from playwright.async_api import async_playwright
import asyncio


async def get_ipl_live_score():

    browser = None

    try:

        print("Launching browser...")

        async with async_playwright() as p:

            # Launch browser
            browser = await p.chromium.launch(
                headless=False,
                slow_mo=500
            )

            # Create browser context
            context = await browser.new_context(
                viewport={"width": 1400, "height": 900},
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/125.0.0.0 Safari/537.36"
                )
            )

            # Open new page
            page = await context.new_page()

            print("Opening Google...")

            # Open Google
            await page.goto(
                "https://www.bing.com",
                timeout=60000
            )

            # Wait for search box
            await page.wait_for_selector(
                "textarea[name='q']",
                timeout=15000
            )

            print("Searching IPL live score...")

            # Enter search query
            await page.fill(
                "textarea[name='q']",
                "today ipl match live score"
            )

            # Press Enter
            await page.keyboard.press("Enter")

            # Wait for results
            await page.wait_for_load_state("networkidle")

            # Bot detection check
            page_text = await page.content()

            if "unusual traffic" in page_text.lower():
                print("Bot detection triggered.")
                return

            print("Opening first search result...")

            # Click first result
            await page.locator("h3").first.click()

            # Wait for page load
            await page.wait_for_load_state("domcontentloaded")

            # Wait extra for dynamic score loading
            await page.wait_for_timeout(5000)

            print("Fetching live score...")

            # Try multiple selectors
            score = None

            possible_selectors = [
                ".ds-text-tight-m",
                ".cb-min-bat-rw",
                ".match-score",
                "[class*='score']",
                "text=/\\d+\\/\\d+/"
            ]

            for selector in possible_selectors:

                try:
                    element = page.locator(selector).first

                    if await element.count() > 0:

                        score = await element.inner_text()

                        if score.strip():
                            break

                except:
                    pass

            if score:
                print("\n==========================")
                print("LIVE IPL SCORE:")
                print(score)
                print("==========================\n")

            else:
                print("Could not fetch live score.")

            # Keep browser open for 10 sec
            await page.wait_for_timeout(10000)

    except Exception as e:

        print("\nERROR OCCURRED:")
        print(type(e).__name__)
        print(str(e))

    finally:

        if browser:
            await browser.close()

        print("Browser closed.")


# Main entry
if __name__ == "__main__":

    asyncio.run(get_ipl_live_score())