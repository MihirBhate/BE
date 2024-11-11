// SPDX-License-Identifier:  License
pragma solidity ^0.8.0;

contract Bank {

    address public accHolder;
    uint256 balance = 0;

    constructor(){
        accHolder = msg.sender;
    }

    function withdraw() public payable{
        require(msg.sender == accHolder, "you are not the account owner.");
        require(balance > 0,"Deposit amount should be greater than 0.");
        balance -= msg.value;
    }

    function deposit() public payable {
        require(msg.sender == accHolder, "You are not the account owner."); 
        require(msg.value > 0, "Deposit amount should be greater than 0."); 
        balance += msg.value; 
    }

    function ShowBlance() public view returns (uint256){
        require(msg.sender == accHolder,"you are not the account owner.");
        return balance;
    } 
}


//install metamask
//change to testnet sepolia
//open sepolia faucet and paste wallet address
//in remix deploy tab open environment and select connected wallets
//then deploy



Explanation of the Solidity Contract: Bank
This smart contract simulates a basic banking system where a user (account holder) can deposit and withdraw funds, 
and check their account balance.

Key Concepts
Smart Contract: A smart contract is a self-executing contract where the terms of the agreement are written into code. 
It runs on the blockchain, which ensures transparency, immutability, and security. The contract is deployed on a 
blockchain like Ethereum.

Solidity: Solidity is the programming language used to write smart contracts for Ethereum. 
It is statically typed and designed to be easy to understand and use for contract development.

Contract Structure
State Variables:

address public accHolder: This variable holds the address of the account holder (owner of the bank account). 
The address is assigned when the contract is deployed. It is set to the address of the person deploying the contract (msg.sender).
uint256 balance = 0: This variable stores the account balance. It is initialized to 0 when the contract is deployed and gets updated 
when deposits or withdrawals are made.
