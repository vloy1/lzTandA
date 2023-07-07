from web3 import Web3
import time
import random
from web3.middleware import geth_poa_middleware

t = 5

arb = {
    'name':'Arbitrum',
    'RPC':'https://arb1.arbitrum.io/rpc',
    'nomer': 110,
    'token': 1000000,
    'gas': 2500000
}

abi_goerli ='[{"inputs":[{"internalType":"address","name":"_weth","type":"address"},{"internalType":"address","name":"_oft","type":"address"},{"internalType":"address","name":"_swapRouter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"oft","outputs":[{"internalType":"contract IOFTCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolFee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"to","type":"address"},{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"adapterParams","type":"bytes"}],"name":"swapAndBridge","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"swapRouter","outputs":[{"internalType":"contract ISwapRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"weth","outputs":[{"internalType":"contract IWETH","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'

def wallett():
    try:
        private = open('wal.txt','r').read().splitlines()
        wallet = private[00]
        return wallet
    except:
        print('Кошельки кончились')

def wallett_del():
    ish = open('wal.txt','r').readlines()
    del ish[00]
    with open("wal.txt", "w") as file:
        file.writelines(ish)

def wallet_aptos():
    wi = open('walet_aptos.txt','r').readlines()
    w = wi[00]
    del wi[00]
    with open('walet_aptos.txt','w') as file:
        file.writelines(wi)
    return w

def status(tx_hash):
    time.sleep(35)
    w3 = Web3(Web3.HTTPProvider(arb['RPC'])) 
    try:
        status_ = w3.eth.get_transaction_receipt(tx_hash)
        status  = status_["status"]
        return status
    except:
        time.sleep(60)
        try:
            status_ = w3.eth.get_transaction_receipt(tx_hash)
            status  = status_["status"]
            return status
        except:
            print("ошибка")
            return 0 

def aptos(ak): ########### gotov
    w3 = Web3(Web3.HTTPProvider(arb['RPC']))
    contractToken = Web3.to_checksum_address('0x1bacc2205312534375c8d1801c27d28370656cff')
    contract = w3.eth.contract(address=contractToken, abi='[{"inputs":[{"internalType":"address","name":"_layerZeroEndpoint","type":"address"},{"internalType":"uint16","name":"_aptosChainId","type":"uint16"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"},{"indexed":false,"internalType":"uint256","name":"unlockTime","type":"uint256"}],"name":"EnableEmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes","name":"_payload","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"_reason","type":"bytes"}],"name":"MessageFailed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountLD","type":"uint256"}],"name":"Receive","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"}],"name":"RegisterToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes32","name":"_payloadHash","type":"bytes32"}],"name":"RetryMessageSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"bytes32","name":"to","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"amountLD","type":"uint256"}],"name":"Send","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"aptosChainId","type":"uint16"}],"name":"SetAptosChainId","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"bridgeFeeBP","type":"uint256"}],"name":"SetBridgeBP","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"paused","type":"bool"}],"name":"SetGlobalPause","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"localChainId","type":"uint16"}],"name":"SetLocalChainId","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"_type","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_minDstGas","type":"uint256"}],"name":"SetMinDstGas","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"precrime","type":"address"}],"name":"SetPrecrime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"bool","name":"paused","type":"bool"}],"name":"SetTokenPause","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_path","type":"bytes"}],"name":"SetTrustedRemote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"SetTrustedRemoteAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"useCustomAdapterParams","type":"bool"}],"name":"SetUseCustomAdapterParams","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"weth","type":"address"}],"name":"SetWETH","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountLD","type":"uint256"}],"name":"WithdrawFee","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountLD","type":"uint256"}],"name":"WithdrawTVL","type":"event"},{"inputs":[],"name":"BP_DENOMINATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SHARED_DECIMALS","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"accruedFeeLD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"aptosChainId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bridgeFeeBP","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"emergencyWithdrawEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"emergencyWithdrawTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"enabled","type":"bool"}],"name":"enableEmergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"failedMessages","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"_configType","type":"uint256"}],"name":"getConfig","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"}],"name":"getTrustedRemoteAddress","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"globalPaused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"isTrustedRemote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"ld2sdRates","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lzEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"}],"name":"minDstGasLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"nonblockingLzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"pausedTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"precrime","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"}],"internalType":"struct LzLib.CallParams","name":"_callParams","type":"tuple"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"quoteForSend","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"registerToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"retryMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"internalType":"uint256","name":"_amountLD","type":"uint256"},{"components":[{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"}],"internalType":"struct LzLib.CallParams","name":"_callParams","type":"tuple"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"sendETHToAptos","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"internalType":"uint256","name":"_amountLD","type":"uint256"},{"components":[{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"}],"internalType":"struct LzLib.CallParams","name":"_callParams","type":"tuple"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"sendToAptos","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_aptosChainId","type":"uint16"}],"name":"setAptosChainId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bridgeFeeBP","type":"uint256"}],"name":"setBridgeFeeBP","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_paused","type":"bool"}],"name":"setGlobalPause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint16","name":"_packetType","type":"uint16"},{"internalType":"uint256","name":"_minGas","type":"uint256"}],"name":"setMinDstGas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_precrime","type":"address"}],"name":"setPrecrime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"bool","name":"_paused","type":"bool"}],"name":"setTokenPause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_path","type":"bytes"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"setTrustedRemoteAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_useCustomAdapterParams","type":"bool"}],"name":"setUseCustomAdapterParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_weth","type":"address"}],"name":"setWETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"supportedTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"trustedRemoteLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"tvlSDs","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"useCustomAdapterParams","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"weth","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_to","type":"address"}],"name":"withdrawEmergency","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amountLD","type":"uint256"}],"name":"withdrawFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint64","name":"_amountSD","type":"uint64"}],"name":"withdrawTVL","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    nonce = w3.eth.get_transaction_count(ak[0])
    gas_price = w3.eth.gas_price
    amointIn = random.randint(10000000000000,90000000000000)
    value = (amointIn/10**18 + 0.00031)
    value = Web3.to_wei(value, 'ether')
    aptos_adres = wallet_aptos()
    tx = contract.functions.sendETHToAptos(
        aptos_adres,
        amointIn,
        [ak[0],
        '0x0000000000000000000000000000000000000000'],
        f'0x00020000000000000000000000000000000000000000000000000000000000002710000000000000000000000000000000000000000000000000000000000007f0d0{aptos_adres[2:]}'
    ).build_transaction(
        {
        'from': ak[0],   
        'value': value,
        'gas': 4500000,
        'gasPrice': gas_price,
        'nonce': nonce,
        })
    signed_txn = w3.eth.account.sign_transaction(tx, private_key=ak[1])
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    s = status(tx_hash)
    print(f'Перевел в aptos  {amointIn} ETH ({s})')

def goerli(ak): ########### gotov
    w3 = Web3(Web3.HTTPProvider(arb['RPC']))
    contractToken = Web3.to_checksum_address('0x0a9f824c05a74f577a536a8a0c673183a872dff4')
    contract = w3.eth.contract(address=contractToken, abi=abi_goerli)
    nonce = w3.eth.get_transaction_count(ak[0])
    gas_price = w3.eth.gas_price
    amointIn = random.randint(10000000000000,90000000000000)
    value = (amointIn/10**18 + 0.00018)
    value = Web3.to_wei(value, 'ether')
    tx = contract.functions.swapAndBridge(
        amointIn,
        0,
        154,
        ak[0],
        ak[0],
        '0x0000000000000000000000000000000000000000',
        b''
    ).build_transaction(
        {
        'from': ak[0],   
        'value': value,
        'gas': 4000000,
        'gasPrice': gas_price,
        'nonce': nonce,
        })
    signed_txn = w3.eth.account.sign_transaction(tx, private_key=ak[1])
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    s = status(tx_hash)
    print(f'перевел в тестнет ({s})')

def res_balance(adres):
    w3 = Web3(Web3.HTTPProvider(arb['RPC'])) 
    eth_balance = w3.eth.get_balance(adres)
    if eth_balance > 0:
        return 1
    else:
        return 0

def aka(privat):
    w3 = Web3(Web3.HTTPProvider(arb['RPC']))
    account = w3.eth.account.from_key(privat)
    adress = account.address
    nativ = res_balance(adress)
    if nativ == 1:
        return adress,privat
    else:
        print('no nativ token')
        return 0,0

def ran(ak):
    wal = aka(ak)
    print(wal[0])
    aptos(wal)
    goerli(wal)
    time.sleep(t)

def main():
    while True:
        ak = wallett()
        print('--------------------------------------------------------')
        ran(ak)
        print('--------------------------------------------------------')
        wallett_del()

main()
