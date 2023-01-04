# NFT Contract

This repository contains the Solidity contracts and Python/Brownie scripts to create NFTs and host the metadata on IPFS. The contract allows users to create these NFT collectibles with a randomly selected picture of a dog.

## Table of Contents

-   [Installation Instructions](https://github.com/coltonmilbrandt/nft-demonstration#installation-instructions)
-   [Deploy](https://github.com/coltonmilbrandt/nft-demonstration#usage)
-   [IPFS](https://github.com/coltonmilbrandt/nft-demonstration#ipfs)

## Installation Instructions

1. Install Python 3.6 or higher
2. Install the Brownie library: `pip install brownie`
3. Clone this repository `git clone https://github.com/coltonmilbrandt/nft-demonstration.git`

## Usage

### Deploy and Create

This script deploys the AdvancedCollectible contract and creates a new collectible. To run the script:

```bash
brownie run scripts deploy_and_create.py
```

> Note: be sure to set your preferred network flag and set up your brownie config

## IPFS

In this NFT contract, IPFS is used to store the metadata for each collectible, including the URL for the image file.

The set_tokenuri.py script sets the token URI for each NFT collectible to the IPFS address of the metadata file. This URI can then be used to retrieve the metadata for the collectible, including the image URL.

The metadata files are stored on IPFS using the ipfs:// protocol. In the set_tokenuri.py script, the IPFS addresses of the metadata files are stored in the dog_metadata_dic dictionary, with the breed of the dog as the key and the IPFS address as the value. The set_tokenURI function is called with the token ID, the contract, and the IPFS address of the metadata file as arguments, and uses the setTokenURI function to set the URI for the collectible.

# Contact Me

### Email me at coltonmilbrandt@gmail.com!

### Check out my website [www.coltonmilbrandt.com](https://coltonmilbrandt.com/)
