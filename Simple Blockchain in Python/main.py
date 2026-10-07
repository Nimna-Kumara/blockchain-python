from blockchain import Blockchain

# Create blockchain
blockchain = Blockchain()

# Add blocks
blockchain.add_block("Alice sends 10 BTC to Bob")
blockchain.add_block("Bob sends 5 BTC to Charlie")
blockchain.add_block("Charlie sends 2 BTC to David")

# Display blockchain
blockchain.display()

is_valid = blockchain.is_valid()
print(f"Validation: {is_valid}")