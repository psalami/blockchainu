# Messages in the Bitcoin network

## When a node connects
 * handshake

## Inventory Messages ("INV")
 * Lets other nodes know that a block has been found by you or that you have a found block from someone else.
 * Uses "INV block" to propagate a block, "INV transaction" to propagate a transaction. Other nodes can use "GETDATA <block or tx hash>" to get block / tx

## Am I synced up?
 * after you connect, you will send a "GETBLOCKS <HashOfOurLatestBlock>" - gets hashes for up to 500 next blocks
 * Send "GETDATA <blockhash>" for any of the 500 bock hashes returned from GETBLOCKS.
 * Call GETBLOCKS again until you have all the latest blocks

## ALERT message
 * used by core devs in emergencies
 * last used early 2013

## PING / PONG messages
 * PING specifies a nonce
 * response is PONG with the same nonce


## Partial nodes

### Simplified Payment Verification (SPV) Protocol ###
  * Do not download the entire blockchain
    * only downloads headers
    * does not download all blocks
      * uses filters: when downloading transactions from other nodes, only download transactions for particular addresses:
        * FILTERADD
        * FILTERCLEAR
      * Privacy Risk
        * I can tell what addresses are yours
        * Use Bloom Filters instead
          * You can tweak accuracy / privacy
          - M hashes
          - N bits (Filter length)
      * Security Risk: nodes may not be honest
  * handy for limited capacity devices
  * After connecting, send "GETHEADERS"
  * Use Merkle Paths to verify transactions
   * Merkle Root summarizes a block's transactions
   
   
## Unconfirmed Transactions

* Unconfirmed transactions are stored in memory until confirmed; transactions are discarded as invalid after a period of time (about a week) has passed
without confirmation.

* Must be linked to a set of "parents": the previous transaction's outputs
* If parent is unknown, put in "orphan pool"
 * When parent is received, recursively "un-orphan"
 
## What can I do with this?
 * Analytics
  * Coinometrics.com
  * Coinalytics.co
  * BitNodes
  * Confidence Ratings blockcypher, sochain.com
  
  
# Coinbeyond
brings bitcoin into the early majority segment of the market.
 * bitcoin Point-of-Sale system
 * Based in Seattle
 * Coinbeyond.com
 * available in Android App store
 
# Ripple labls
* Cotius - hosting platform for decentralized application

# Talkbowl
E-Commerce marketing company
* How to solve chargeback problem with Bitcoin

# Skuchain
* silently rebels against the Federal Reserve


# Midterm projects

register or join a team http://bit.ly/bcuprojects
* must use one or more of: Block, Create/Sign/Query Transaction
 * bonus points: non bitcoin/financial use, combination with other crypto technology
* Demo day on Jan 31st

* Awards (eternal glory on the blockchain)
 * Innovator's award (judged by the panel)
 * Moon Shot (judged by the panel)
 
## think from blockchain primitives
* append only: notarization
* public/ priv key baesd access
* transparent & enforced logic
* native store of value
* tokenization
* evergreen data - tech can evolve even if original developer becomes disinterested

## Checklist

* Does it:
 * benefit from one or more of the primitives of blockchain?
 * reduce counterparty risk involved?
 * reduce intermediate parties / gate keepers?
 * make attack harder / more expensive (i.e. private blockchain for enterprise storage / accounting (see subledger))
 * make post fact auditing easier?
 * make other developers more likely to adopt due to blockchain's openness

moonshot: i.e. pabble.io currency with decentralized reserve bank


### projects that need assistance
* micropayments for wifi access
* multisig to connect bitcoin to other payment networks in node.js - Steven Zeiler from codius



