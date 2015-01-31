import sys
import bitcoin.rpc
from bitcoin.core import *
from bitcoin.core.serialize import *
from bitcoin.core.script import *

bitcoin.SelectParams('testnet')
proxy = bitcoin.rpc.Proxy(service_port=18332)

def declare_trust(message):
	
	unspent = sorted(proxy.listunspent(0), key=lambda x: hash(x['amount']))

	txins = [CTxIn(unspent[-1]['outpoint'])]
	value_in = unspent[-1]['amount']

	change_addr = proxy.getnewaddress()
	change_pubkey = proxy.validateaddress(change_addr)['pubkey']
	change_out = CMutableTxOut(MAX_MONEY, CScript([change_pubkey, OP_CHECKSIG]))

	message_outs = [CMutableTxOut(0, CScript([OP_RETURN, VarStringSerializer.serialize(bytes(message, 'UTF-8'))]))]
	tx = CMutableTransaction(txins, message_outs)

	FEE_PER_BYTE = 0.00025*COIN/1000
	while True:
		tx.vout[0].nValue = int(value_in - max(len(tx.serialize()) * FEE_PER_BYTE, 0.00011*COIN))

		r = proxy.signrawtransaction(tx)
		assert r['complete']
		tx = r['tx']

		if value_in - tx.vout[0].nValue >= len(tx.serialize()) * FEE_PER_BYTE:
			print(b2x(tx.serialize()))
			print(len(tx.serialize()), 'bytes', file=sys.stderr)
			print(b2lx(proxy.sendrawtransaction(tx)))
			break

declare_trust("msVEpLmvQhWoBE41BbjapcczcsX93xaLB3")