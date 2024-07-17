import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index: {self.index}, previous_hash: {self.previous_hash}, timestamp: {self.timestamp}, data: {self.data}, hash: {self.hash})"

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}".encode()
    return hashlib.sha256(value).hexdigest()

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    previous_hash = previous_block.hash
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_blocks_to_add = 10

for i in range(num_blocks_to_add):
    data = f"Block {i + 1} data"
    new_block = create_new_block(previous_block, data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block #{new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")

for block in blockchain:
    print(block)
