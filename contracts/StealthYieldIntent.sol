// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract StealthYieldIntent {
    struct YieldIntent {
        address user;
        uint256 yieldTarget; // Annual % yield (e.g., 10% -> 1000)
        uint256 timestamp;
    }

    mapping(address => YieldIntent) public yieldIntents;

    event IntentSubmitted(address indexed user, uint256 yieldTarget);

    function submitIntent(uint256 _yieldTarget) public {
        yieldIntents[msg.sender] = YieldIntent({
            user: msg.sender,
            yieldTarget: _yieldTarget,
            timestamp: block.timestamp
        });

        emit IntentSubmitted(msg.sender, _yieldTarget);
    }

    function getIntent(address _user) public view returns (YieldIntent memory) {
        return yieldIntents[_user];
    }
}
