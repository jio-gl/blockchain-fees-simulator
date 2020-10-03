# blockchain-fees-simulator

## Introduction

Current 1st Price Auction of transactions fees to be included a in a block in Ethereum is leading to price spikes under congestion scenarios [3]:

> Ethereum’s existing gas prices respond to the relatively limited number of transactions that one can facilitate using a single block. Miners, in such a scenario, can choose the highest-priced transactions as their priority, so the result is an increase in effective gas prices.

## Description

A simulation tool for blockchain fees, aka gas market in Ethereum-type blockchains.

We want to compare at least the following strategies:

 - Bitcoin/Ethereum standard 1st Price Auction.
 - Ethereum EIP-1599, floating minimum gas-price, currently implemented in the Celo Blockchain.
 - Experimental Dutch-auction strategies.
 
We plan to use syntethic data and also empiric registered data from transaction mempool, such as published by Blocknative [0].

## Bibliography

[0] Evidence of Mempool Manipulation on Black Thursday: Hammerbots, Mempool Compression, and Spontaneous Stuck Transactions https://blog.blocknative.com/blog/mempool-forensics

[1] Blockchain fees are broken. Here are 3 proposals to fix them. https://haseebq.com/blockchain-fees-are-broken/

[2] Ethereum's Growing Gas Crisis (And What's Being Done to Stop It) https://www.coindesk.com/ethereums-growing-gas-crisis-and-whats-being-done-to-stop-it

[3] Ethereum scalability issues exposed as high gas fees stall DeFi boom https://cointelegraph.com/news/ethereum-scalability-issues-exposed-as-high-gas-fees-stall-defi-boom

[4] A transaction pricing mechanism that includes fixed-per-block network fee that is burned and dynamically expands/contracts block sizes to deal with transient congestion. https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md
