//const {artifacts} = require("truffle"); 
const testCon = artifacts.require("testCon");

module.exports = function (deployer) {
    deployer.deploy(testCon);
};
