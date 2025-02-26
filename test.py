import unittest
from labka1 import BlockProcessor

class TestBlockProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = BlockProcessor()

    def test_add_block_success(self):
        block = {'id': 1, 'view': 0}
        result = self.processor.add_block(block)
        self.assertTrue(result)
        self.assertIn(1, self.processor.blocks)
        self.assertEqual(self.processor.blocks[1], 0)

    def test_add_block_duplicate(self):
        block = {'id': 1, 'view': 0}
        self.processor.add_block(block)
        result = self.processor.add_block(block)
        self.assertFalse(result)
        self.assertEqual(len(self.processor.blocks), 1)

    def test_make_blockchain(self):
        block1 = {'id': "1", 'view': "0"}
        block2 = {'id': "2", 'view': "2"}
        block3 = {'id': "3", 'view': "1"}
        self.processor.add_block(block1)
        self.processor.add_block(block2)
        self.processor.add_block(block3)
        self.processor.add_vote({'id': "1"})
        self.processor.add_vote({'id': "2"})
        self.processor.add_vote({'id': "3"})
        result = self.processor.make_blockchain()
        self.assertEqual(result, ["1", "3", "2"])

if __name__ == '__main__':
    unittest.main()