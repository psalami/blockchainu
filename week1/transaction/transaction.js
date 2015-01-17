var bitcoin = require('bitcoinjs-lib');
var Chain = require('chain-node');
var chain = new Chain({
	blockChain: "testnet3"
});


var tx = new bitcoin.TransactionBuilder();
tx.addInput("48121ab50d934bea8cac1fc0db497459a256d5d508fd4d9d0a771a6113b6d2ae", 0);
tx.addOutput("mxLGBf5Lgih9odquUDYQQYoPpvvkaHrWYt", 50000);
tx.addOutput("mxLGBf5Lgih9odquUDYQQYoPpvvkaHrWYt", 50000);
tx.addOutput("mpXKGuh1YmgxuP7sTPtDCY2cJ7VYXjGwk6", 100000);

var key = bitcoin.ECKey.fromWIF("KxmVMvfqwnXS1Dgrm3TLhVw4aZd2qs3xTwpNgfWsFJ9wPuHCrEDZ");
tx.sign(0, key);

var signedHex = tx.build().toHex();
console.log(signedHex);

chain.sendTransaction(signedHex, function(err, resp){
	if(err){
		console.log("err:");
		console.log(err);
	}
	console.log("resp:");
	console.log(resp);
});

