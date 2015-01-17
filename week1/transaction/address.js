var bitcoin = require('bitcoinjs-lib');

var key = bitcoin.ECKey.makeRandom();
console.log(key.toWIF());
console.log(key.pub.getAddress(bitcoin.networks.testnet).toString());