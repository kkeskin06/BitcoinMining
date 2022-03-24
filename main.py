from hashlib import sha256
import time

def _SHA256(val):
    return sha256(val.encode()).hexdigest()

def mine(transactions,previous_hash,difficulty):
    prefix_zeros = '0'*difficulty
    nonce = 0
    while True:
        nonce += 1
        val = transactions + previous_hash + str(nonce)
        hash = _SHA256(val)
        if(hash.startswith(prefix_zeros)):
            print(f"nonce bulundu : {nonce}")
            return hash

def main():
    difficulty = 6
    transaction = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    previous_hash = "00000000000000000006a1ba16249c80054748dae3425149925cd09a2933019e"
    start_time = time.time()
    print("mining basladi...")
    hash = mine(transaction,previous_hash,difficulty)
    total_time = str(time.time() - start_time)
    print(f"Mining {total_time} surede bulundu..")
    print(f"Hash : {hash}")

main()
