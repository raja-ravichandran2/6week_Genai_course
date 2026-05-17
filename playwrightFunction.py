from playwright.async_api import async_playwright
import asyncio


async def pwFunction():

    async with async_playwright() as p:

        # Launch browser
        browser = await p.chromium.launch(
            headless=False
        )

        # Create page
        page = await browser.new_page()

        # Open Google
        await page.goto("https://www.google.com")

        # Wait for page load
        await page.wait_for_timeout(3000)

        # Type search text
        await page.fill(
            "textarea[name='q']",
            "yesterday ipl match stats"
        )

        # Press Enter
        await page.keyboard.press("Enter")

        # Wait for results
        await page.wait_for_timeout(5000)

        print("Search completed.")

        # Close browser
        await browser.close()


# Main entry
if __name__ == "__main__":
    asyncio.run(pwFunction())