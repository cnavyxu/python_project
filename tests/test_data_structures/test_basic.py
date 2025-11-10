"""
基本数据结构测试
"""

import pytest
from src.data_structures import LinkedList, Stack, Queue


class TestLinkedList:
    
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]
    
    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        assert ll.to_list() == [3, 2, 1]
    
    def test_delete(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.delete(2)
        assert ll.to_list() == [1, 3]


class TestStack:
    
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
    
    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2
    
    def test_empty(self):
        stack = Stack()
        assert stack.is_empty()
        stack.push(1)
        assert not stack.is_empty()


class TestQueue:
    
    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
    
    def test_empty(self):
        queue = Queue()
        assert queue.is_empty()
        queue.enqueue(1)
        assert not queue.is_empty()
