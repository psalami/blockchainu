
# Bitcoin Scripting

Presented by Matthieu - CTO of BlockCypher
* Former VP @ Apache
* rebuilt a full node

## Intro

Scripts allow Spending
* Script returns true (spending is valid) or false (spending is invalid)
* Match output script with spending input script
  * Input script: scriptSig 
  * output script: scriptPubKey
* An output / input pair is an invocation
* Output script: like a function
* Input script: like parameters to the function

## Stack-based language
 * Similar to Reverse Polish Notation
 * Advantageous for Bitcoin because it is easy to implement, compact (uses little memory), portable and easy to read
 * Everything is a byte array
 * Instructions are byte arrays 
 * Conditions but no loops purposefully (see ethereum)
 * Operatrions (called opcodes)
   * single byte per operation (max 256)
   * are often represented as hex
   * comparison
   * arithmetic
   * crypto primitives (OP_RIPEMD160, OP_HAS256, OP_CHECKSIG, OP_CHECKMULTISIG)
  
## Evaluation Logic
 1. Start with an empty stack
 2. Evaluate the scriptSig (output to be spent)
 3. evaluate the script
 4. if result is true(1), transaction is good, otherwise invalid
 
## Example  - Password locked

## Standard Scripts
* an invalid script (and transaction) will not be accepted
* a non-standard script (and transaction) will not be relayed. But miners can still include them (i.e. Eligius mining pool will accept your
non-standard script into a block that it mines. However, this means you would have to wait 6x - 7x longer than standard transaction in order
 for the transaction to be accepted to a block)
 
## Pay to Pubkey Hash

### send funds

OP_DUP [duplicates what is on top of the stack - the new input]
OP_HASH160
0x14 [14 bytes to follow]
0x89ABCDEF[...][this big hex is what we call an address]
OP_EQUALVERIFY [check for equality]
OP_CHECKSIG [check the signature]  


### redeem funds

## Pay to Pubkey

### Send
0x14  
024d57[...]  
OP_CHECKSIG  

### Redeem
<sig>

Only used in mining in older coinbase transactions 


## Null Data
OP_RETURN  
<up to 40 bytes of data>

* Allows embedding data in the block chain
* Non-redeemable (burned)
* Provably prunable
* applications in document signing


## Plain Multisig

### Send
OP_2  
<pk1><pk2><pk3>  
OP_3  
OP_CHECKMULTISIG [most "magical" function in the Bitcoin stack]  

### Redeem
<sig1><sig2>

* max 2 out of 3
* new generally replaced by Pay-to-ScriptHash (does not reveal public keys)

## Pay to Script Hash

most complicated  

### Send
OP_HASH160  
e4672a0ad[...]  
OP_EQUAL  

### Redeem
<any script that hashes to the above value>  

* evaluation has a special rule (bip 16)
  * check that hashing the script matches the hash in the scriptSig
  * construct a new stack with that script
  * exeute the embedded script (has to be standard)
  
* mostly used for multisig embedded transactions

### Example

OP_2  
0x41  
0x049[...]
...
OP_FALSE [due to bug in bitcoin core]    
0x48
0x3045[...]
0x49  
0x3046[...]  
OP_PUSHDATA1 0xc9  
0x**5241**0491bba[...]



