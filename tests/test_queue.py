import unittest
from stack2queue.queue import StackQueue


class QueueTests(unittest.TestCase):

    def test_dequeue_on_empty_queue(self):
        queue = StackQueue()
        self.assertTrue(queue.isEmpty())
        with self.assertRaises(ValueError):
            queue.dequeue()

    def test_size(self):
        queue = StackQueue(*range(100))
        self.assertEqual(queue.size(), 100)

    def test_enqueue_with_init(self):
        queue = StackQueue(1, 2, 3)
        self.assertFalse(queue.isEmpty())
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_get(self):
        queue = StackQueue(1, 2, 3)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.get(), 1)
        self.assertEqual(queue.size(), 3)
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(4, 5)
        queue.dequeue()
        self.assertEqual(queue.get(), 4)

    def test_enqueue_dequeue(self):
        queue = StackQueue(1, 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.isEmpty())
        with self.assertRaises(ValueError):
            queue.dequeue()
        queue.enqueue(3, 4, 5)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)
        self.assertTrue(queue.isEmpty())
        with self.assertRaises(ValueError):
            queue.dequeue()

    def test_iter(self):
        self.assertEqual(list(StackQueue()), [])
        queue = StackQueue(1, 2, 3, 4, 100)
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(3, 4, 5)
        queue.dequeue()
        self.assertEqual(list(queue), [4, 100, 3, 4, 5])

    def test_iter_with_one_element(self):
        queue = StackQueue(1)
        self.assertEqual(list(queue), [1])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
