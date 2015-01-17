# Transaction example

This Node.js sample code generates a wallet address and then sends funds from that wallet to another address or to itself. It relies on the [bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib) library and the [chain.com](http://www.chain.com) API to generate the wallet and make the transaction, respectively.

## Requirements
* node.js v0.10.26 or greater (might work with previous versions but untested)

## Installation
clone this repository, navigate to the transaction project directory and install the required Node.js dependencies:

```
git clone https://github.com/psalami/blockchainu.git
cd blockchainu/week1/transaction
npm install
```

## Usage
1) generate a new wallet private key and public bitcoin address (this will create an address in the Bitcoin testnet):

```
node address.js
```

Save the output of this command in a separate file. The first line is your private wallet and the second line is your public address.

2) Send funds to the public address. You can do this, for example, by using a public testnet Bitcoin faucet such as http://faucet.haskoin.com/.

3) Wait for your funds to arrive in your wallet: use a blockchain explorer to verify that the transaction was confirmed, such as http://explorer.chain.com. Note the transaction hash.

4) Edit transaction.js: replace the value in the addInput line with your transaction hash; replace the values in the addOutput line with the destination address where you would like to send the funds; use the second argument to the addOutput function to indicate the amount to send (in Satoshi). You may add as many addOutput lines as you'd like.

5) run the transaction code:

```
node transaction.js
```