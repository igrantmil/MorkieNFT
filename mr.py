import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

async def mint_0g_panda():
    print("Launching browser...")
    browser = await launch(
        headless=False,
        args=['--start-maximized', '--no-sandbox']
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})

    print("Navigating to mint page...")
    await page.goto('https://morkie.xyz/og', waitUntil='networkidle2')

    try:
        print("Waiting for wallet connect button...")
        await page.waitForSelector('button.wallet-connect', timeout=20000)
        await page.click('button.wallet-connect')
        print("Wallet connect button clicked.")
    except TimeoutError:
        print("Wallet connect button not found! Please check the selector or connect manually.")

    print("Please complete wallet connection in the browser if needed.")
    input("Press Enter after your wallet is connected...")

    try:
        print("Waiting for mint button...")
        await page.waitForSelector('button.mint-button', timeout=30000)
        await page.click('button.mint-button')
        print("Mint button clicked.")
    except TimeoutError:
        print("Mint button not found! Please check the selector or page state.")
        await browser.close()
        return

    try:
        print("Waiting for mint success confirmation...")
        await page.waitForSelector('.mint-success', timeout=60000)
        print("Minting completed successfully!")
    except TimeoutError:
        print("Mint success message not found. Please check if minting succeeded.")

    await browser.close()

if __name__ == "__main__":
    asyncio.run(mint_0g_panda())
