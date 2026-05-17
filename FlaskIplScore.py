from flask import Flask, jsonify
from playwright.async_api import async_playwright
import asyncio
import webbrowser

app = Flask(__name__)


async def get_ipl_live_score():

    browser = None

    try:

        async with async_playwright() as p:

            print("Launching browser...")

            # Visible browser
            browser = await p.chromium.launch(
                headless=False,
                slow_mo=500
            )

            page = await browser.new_page()

            print("Opening Bing...")
            

            await page.goto(
                "https://www.bing.com",
                timeout=60000
            )
            print("Waiting for search box...")
            await page.wait_for_selector(
                "textarea[name='q']",
                timeout=15000
            )

            print("Searching IPL score...")

            await page.fill(
                "textarea[name='q']",
                "today IPL live stats",
            )

            await page.keyboard.press("Enter")

            await page.wait_for_load_state(
                "networkidle"
            )

            # Wait to see browser actions
            await page.wait_for_timeout(3000)

            score = None

            selectors = [
                "[class*='score']",
                "text=/\\d+\\/\\d+/"
            ]

            for selector in selectors:

                try:

                    element = page.locator(selector).first

                    if await element.count() > 0:

                        score = await element.inner_text()

                        if score.strip():
                            break

                except:
                    pass
            result = {
                "status": "success",
                "score": score
            }
    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

    finally:

        if browser:
            await browser.close()

        print("Browser closed")

        return result


@app.route("/")
def home():
    return """
    <h1>IPL Live Score Flask App</h1>
    <a href='/iplscore'>Click Here To Get IPL Score</a>
    """


@app.route("/iplscore")
def iplscore():

    result = asyncio.run(
        get_ipl_live_score()
    )

    return jsonify(result)


if __name__ == "__main__":

    # Auto open browser
    webbrowser.open(
        "http://127.0.0.1:5000"
    )

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )