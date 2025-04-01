class BlockProcessor:
    def __init__(self):
        self.blocks = {}
        self.votes = []
        self.blockchain = []
        self.current_view = 0

    def add_block(self, block):
        if block['id'] in self.blocks:
            return False
        self.blocks[block['id']] = block["view"]
        return True

    def add_vote(self, vote):
        if vote['id'] in self.votes:
            return False
        self.votes.append(vote["id"])
        return True
        
    def make_blockchain(self):
        self.blocks = sorted(self.blocks.items(), key=lambda x: x[1])
        for block_id, view in self.blocks:
            if block_id in self.votes and int(view) == self.current_view:
                self.blockchain.append(block_id)
                self.current_view += 1
                self.votes.remove(block_id)
        return self.blockchain

    def get_input(self):
        while True:
            command = input("Enter command (block/vote/exit): ")
            if command == "exit":
                break
            elif command == "block":
                block_id = input("Enter block id: ")
                view = input("Enter view: ")
                self.add_block({"id": block_id, "view": view})
            elif command == "vote":
                vote_id = input("Enter vote id: ")
                self.add_vote({"id": vote_id})
            else:
                print("Invalid command")

if __name__ == "__main__":
    processor = BlockProcessor()
    processor.get_input()
    print("Final blockchain:", processor.make_blockchain())