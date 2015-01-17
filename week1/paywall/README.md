# Bitcoin Paywall

This application implements a simple paywall that does not require a sign-up. It does not store any state in the browser or on the server.
Instead, it relies on the Bitcoin blockchain to verify payment.
The paywall application interfaces with the blockchain via the [block.io](http://www.block.io) API. A token only known to the user is used to identify a block.io wallet. If the wallet has
a balance equal to or greater than the price of the content (as defined by the CONTENT_PRICE variable in paywall.py), access to the content is granted.
Otherwise, the user is redirected to a page where a payment can be made. Once payment is confirmed, the user is granted a token to access the content.

## Requirements
* Python 2.7.x
* HTTP port 5000 should be open

## Installation
1) clone this repository and change to the paywall directory:

```
git clone https://github.com/psalami/blockchainu.git
cd blockchainu/week1/paywall
```

2) install the required Python packages:

``pip install -r requirements.txt``

3) optionally, change the price of your content by modifying the `CONTENT_PRICE` variable in paywall.py.

## Usage
1) while still in the paywall directory, start the HTTP server:

``python paywall.py``

2) point your browser at the home page: **http://127.0.0.1:5000**. You will initially be redirected to the token page
where you can submit a payment. Once the payment is received, you will be given a token and a link to access the content.
Save the token for future use; you will be able to enter it when you return at a later time to access the content again.
