//SPDX-License-Identifier: Aditya Patil
pargram Solidity 0.8.0
contract Bank{

    mapping(address=>uint256)  private balanace;

    function create() public{
        balanace[msg.sender] =0;
    }

    function dep(uint256 amount) public payable{
        balanace[msg.sender] += amount;
    }

    function with(uint256 amount) public{
        require(balanace[msg.sender]>=amount , " inn");
        balanace[msg.sender]-=amount;
    }

    function check() public view returns (uint256){
        return balanace[msg.sender];
    }
}

