= Blockchain Web of Trust =

A custom wallet service that shows a balance that includes only coins from a trusted source. This enables many interesting use-cases, for example allowing organizations to issue tokens for volunteer work. Other use-cases include public reviews and fraud prevention. The web of trust ensures that the tokens must be earned and cannot be transferred. 

== Technical Implementaiton ==

We propose a scheme whereby a whitelister can write a list of trusted addresses to the blockchain using OP_RETURN transactions. Each client wallet configures the address of a whitelister. When the wallet reports the user's balance, the wallet checks the senders of its unspent outputs; it traverses the transactions in the blockchain to find all OP_RETURN transactions from the declared whitelister. Certain OP_RETURN transactions will contain a whitelisted address. The reported balance will include only amounts from the unspent outputs where the sender is in the set of whitelisted addresses.


There is a mechanism for a whitelister to establish trust for a certain address: the whitelister sends a message to an entity with whom he wants to establish trust. The entity signs the message with their private key and sends it back to the whitelister. The whitelister can then be confident that the entity with whom he wants to establish trust does indeed control the wallet they will report to the blockchain.


== Usage ==

1) As a whitelister, declare trust for a particular address
```
python3 trusted-wallet.py declare_trust msVEpLmvQhWoBE41BbjapcczcsX93xaLB3
```

2) As a user, check balance for coins traced to a trusted source. The user specifies the whitelister.
```
python3 trusted-wallet.py get_balance mtkmJqRsqMCPc4Dz4RKwWgfxKhUAwAAbzc
```