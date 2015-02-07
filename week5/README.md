# Module 2 - Decentralized Applications

With Tom Ding from Koinify

What qualifies decentralized apps? what is a smart contract?

## Basic Concepts
* Decentralized Autonomous Organization (Vitalik Buterin) / Decentralized Autonomous Organization (Daniel Lerner), etc (many definitions)
  * DAO: profitable
  * DAC: (ethereum) more generalized application; does not necessarily need to be profitable
* Smart contract (secure multi-party computation, on-chain code, etc)
* Smart corporation:
  * replacement for traditional Delaware corp (i.e. corporation lives on blockchain and maintains its ledgers cryptographically)
  * i.e. investor cap table is maintained on blockchain

# consensus components
* shared application state: proof of x
* economics: distribution and incentive: digital tokens that create scarcity
* membership / access control (i.e. eris: blockchains don't all have to be public; access control is maintained by blockchain)
* self-governance (who are the board members, who are the employees, who gets paid out, who has preferred shared, etc)


## Cryptoeconomics
* encourages open & common protocol
* crypto tokens serve to:
  * incentivize developers
  * reward content / app-specific contribution
  * gamification
  * i.e. use crypto-tokens to pay for advertising (using dynamic pricing model)

Developers of crypto-currency and dapp platforms can raise funding more easily through pre-sale of currency (i.e. Ethereum):
classic models of of monetization usually involve some centralized model such as product sales (Apple) or assymetric revenue (i.e. Google Adwords)  
seignorage: via crowdsale, benefit from difference between creating currency and increase in value (rewards devs)  
cap gain: buy tokens early and benefit from appreciation (rewards devs and token holders (i.e. external investors))  
rewards: benefits token holders

## factum
* data layer for blockchain: federated and auditing nodes (semi-private servers)  
* creates two-layer structure: data lives on factum chain and factum chain creats merkle root hash which gets sent to bitcoin blockchain (i.e. using OP_RETURN).
* two-class coin structure: factoid (volatile like other crypto-currencies); entry credit (stable; you can trade factoids for entry credits)

## Deckbound
* first blockchain based trading card game
* colorcoin-like tracking for cards
* http://bitbind.io
* http://deckbound.com
* https://www.youtube.com/watch?v=d_-mxgUNiOM

## Augur
P2P Prediction Market
* "google for the future": i.e. "Who will be president in 2016", "Who will be the next Facebook", "How many printers will HP sell next year"
* wheather insurance, election prediction, enterprise forecast, price discovery (learn how to price a new service), etc
* sidechain + ethereum
* 2-class structure
  * stable coin: stabilization via Seigniorage shares scheme
  * Reputation: Fixed supply. Non-fungible. Use it or lose it.
* Reputation allows nodes to vote on decision outcome



# Koinify

* marketplace for dApps

# Final project
* finalize proposals and team structure: Feb 14th
* internal demo day: Saturday March 7th
* Top Projects Public demo night: Tuesday March 10th
  * signup at meetup.com/blockchainu
  * Attendees: leading crypto startups and VCs
  * must use one or more of the distributed toolkits: filesystem, smart contract, notarization, tokenization, etc

# External asset tracking
* realitykeys (https://www.realitykeys.com)
* shelling coin (see whitepaper)


# Eris

* Thelonius: 
  * https://thelonious.io/tutorials/
  * app server to work with multiple blockchains
  * superset of Ethereum blockchain
  * ability to create own blockchain (set rules: control who can mine, who can transact, write scripts for consensus rules, etc)
  * indexes for data are stored in Ethereum blockchain 
  * javascript lives in dserver so you don't have to pay for Ethereum transactions
  * uses doug to coordinate chain using genesis doug (gendoug)
  * all rules run through gendoug contract
  * when a new block comes in, it first looks up the validate block contract in the gendoug contract (analogous to bootloader or kernel for distributed operating system)
  * every app has its own chain
  * hooks into IPFS (inter-planetary file system - distributed P2P storage system)
  * ability to write ethereum contracts as Thelonium contracts
  * distributed through docker images

* Homework assignment



