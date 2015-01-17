# -- Week 2 Class Notes --

#Bitcoin protocol with Reddit's Ryan X. Charles

## Bitcoin number formats
* BTC uses many different number formats in source code:
 * uses both big endian and little endian numbers
 * Varint: Bitcoin's own number format
 * ScriptNum
 * FixedPoint: always exactly 8 decimal places; used only internally to represent a Satoshi
 * Floating Point: used i.e. to compute difficulty
 * "If a number format exists, bitcoin uses it somewhere"
 
* Public Keys
 * DER format
 * Compressed
 
* Signatures
 * ECDSA: a signature algorithm used by Bitcoin
 * DER format
 * **[h][l][rh][rl][r][sh][sl][s]**
 * h (0x30), (l)ength of what follows, rh (2), rl (length of r), sh (2), sl (length of s)
  * all are 1 byte
  
* Scripts
 * series of operations and data to be pushed to the stack
 * stack, alt stack; no heap
 
* Inputs
 * **[txhashbuf][txoutnum][scriptvi][script][seqnum]**
 
* Outputs
 * **[value][scriptvi][script]**
 * value: UInt64E - number of satoshis to send
 * scriptvi: varint for length of script
 * script: the scriptPubKey - executed before scriptSig
 
* Transactions
 * **[version][txinsvi][txins][txoutsvi][txouts][nlocktime]
 * version: UInt32LE, presently 3
 * txinsvi: Varint, the number of inputs
 * txins: the inputs concatenated together
 * txoutsvi: Varint, the number of outputs
 * nlocktime
 
* Standard Transactions
**pubkeyhash**

scriptSig:
<sig><pubkey>

scriptPubkey
OP_DUP OP_HASH160 <pubkeyhash> OP_EQUALVERIFY OP_CHECKSIG

(standard, obsolete) multisig

scriptSig:
OP_0 <sig> <sig>

scriptPubkey:

m <pubkey> <pubkey> <pubkey> n OP_CHECKMULTISIG

### p2sh multisig
scriptSig:  
OP_0 <sig> <sig> <redeemScript>

redeemScript:
m <pubkey> <pubkey> <pubkey> n OP_CHECKMULTISIG


*** OP_RETURN

scriptPubKey:

OP_RETURN <up to 40 bytes of data>
"provably prunable"

### proof of existence
insert a document into the blockchain in the OP_RETURN field and make a small transaction.  
see http://www.proofofexistence.com
