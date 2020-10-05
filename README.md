# blockchain-fees-simulator

## Introduction

Because the size of blocks in blockchain is limited by network propagation, the miners must have a way to choose which transactions go early and which ones can be left for later blocks [1]:

> But here’s the problem: how does a miner prioritize among potential candidates to get into a block? If there are more candidate transactions than slots in a block, how do we decide what goes where? You might think a egalitarian approach is ideal: everyone is treated equally, and miners include transactions into blocks on a first-come-first-serve basis.

Current First-price Auction of transactions fees to be included a in a block in Ethereum is leading to price spikes under congestion scenarios [3]:

> Ethereum’s existing gas prices respond to the relatively limited number of transactions that one can facilitate using a single block. Miners, in such a scenario, can choose the highest-priced transactions as their priority, so the result is an increase in effective gas prices.

## Description

A simulation tool for blockchain fees, aka gas market in Ethereum-type blockchains.

We want to compare at least the following strategies:

 - Bitcoin/Ethereum standard First-price Auction.
 - Ethereum EIP-1599, floating minimum gas-price, currently implemented in the Celo Blockchain.
 - Experimental Dutch-auction strategies, also called uniform-price auction [5].
 
We plan to use syntethic data and also empiric registered data from transaction mempool, such as published by Blocknative [0].

Our focus is on Dutch-auction/uniform-price to prove that performs better on prices (prices are lower). We also assume that cricismd to Dutch-auction/uniform-price do not sustain:

 - Miner own transactions: if the miner includes its own transactions he can only move the price down he *cannot raise the gas price* if there are transactions for other people to be included in the block;
 - Bribing attacks: the miner can influence transaction senders with bribes or refunds because 1$ change in one transaction can influence all the transactions in the block (> 1$ impact). These criticism do not sustain because to raise gas prices the miner must bribe or influence *all* the transactions to be included in the block.

## Bibliography

[0] Evidence of Mempool Manipulation on Black Thursday: Hammerbots, Mempool Compression, and Spontaneous Stuck Transactions https://blog.blocknative.com/blog/mempool-forensics

[1] Blockchain fees are broken. Here are 3 proposals to fix them. https://haseebq.com/blockchain-fees-are-broken/

[2] Ethereum's Growing Gas Crisis (And What's Being Done to Stop It) https://www.coindesk.com/ethereums-growing-gas-crisis-and-whats-being-done-to-stop-it

[3] Ethereum scalability issues exposed as high gas fees stall DeFi boom https://cointelegraph.com/news/ethereum-scalability-issues-exposed-as-high-gas-fees-stall-defi-boom

[4] A transaction pricing mechanism that includes fixed-per-block network fee that is burned and dynamically expands/contracts block sizes to deal with transient congestion. https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md

[5] First and second-price auctions and improved transaction-fee markets https://ethresear.ch/t/first-and-second-price-auctions-and-improved-transaction-fee-markets/2410
