
# MorkieNFT

**Auto Minting NFT On Morkie**

## Overview

MorkieNFT is a Python automation script that streamlines the process of minting NFTs on the [Morkie OG Mint](https://morkie.xyz/og) platform. Built using [Pyppeteer](https://github.com/pyppeteer/pyppeteer), this tool helps users automate the minting process by interacting with the website's UI, making NFT minting faster and more convenient.

> **⚠️ Warning:**  
> This script is for educational and testing purposes only. Do not use it with wallets containing real funds. Automating wallet interactions (e.g., MetaMask) is inherently risky.

---

## Features

- Opens the Morkie OG minting page automatically
- Clicks the "Connect Wallet" and "Mint" buttons
- Waits for transaction confirmation
- Easy to customize for other similar NFT minting sites

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/igrantmil/MorkieNFT.git
    cd MorkieNFT
    ```

2. **Install dependencies:**
    ```bash
    pip install pyppeteer
    ```

---

## Usage

1. **Make sure you have [Python 3.7+](https://www.python.org/downloads/) installed.**

2. **Run the script:**
    ```bash
    python mr.py
    ```

3. **Follow the on-screen instructions:**
    - A browser window will open.
    - Manually connect your wallet (MetaMask or similar) in the browser.
    - Press Enter in the terminal once your wallet is connected.
    - The script will attempt to mint your NFT.

---

## Configuration

- **Selectors:**  
  If the website changes, update the button selectors in `mint.py`:
    - `button.wallet-connect` for the wallet connect button
    - `button.mint-button` for the mint button
    - `.mint-success` for the success message

- **Headless Mode:**  
  By default, the browser is launched in visible mode (`headless=False`). You can change this in the script if you prefer headless operation.

---

## Disclaimer

- This project is not affiliated with Morkie or any NFT platform.
- Use at your own risk. The author is not responsible for any loss of funds or assets.
- Automating wallet interactions is not recommended for production or with real assets.

---

## License

MIT License

