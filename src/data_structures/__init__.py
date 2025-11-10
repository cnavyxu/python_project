"""
数据结构模块

实现各种常用数据结构
"""

from typing import Optional, Any, List


class Node:
    """链表节点"""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None


class LinkedList:
    """单向链表"""
    
    def __init__(self):
        self.head: Optional[Node] = None
    
    def append(self, data: Any):
        """在末尾添加节点"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data: Any):
        """在开头添加节点"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data: Any):
        """删除节点"""
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def to_list(self) -> List[Any]:
        """转换为列表"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


class TreeNode:
    """二叉树节点"""
    
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:
    """二叉搜索树"""
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, data: Any):
        """插入节点"""
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node: TreeNode, data: Any):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data: Any) -> bool:
        """搜索节点"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node: Optional[TreeNode], data: Any) -> bool:
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)
    
    def inorder_traversal(self) -> List[Any]:
        """中序遍历"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


class Stack:
    """栈"""
    
    def __init__(self):
        self.items: List[Any] = []
    
    def push(self, item: Any):
        """入栈"""
        self.items.append(item)
    
    def pop(self) -> Any:
        """出栈"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self) -> Any:
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """获取栈大小"""
        return len(self.items)


class Queue:
    """队列"""
    
    def __init__(self):
        self.items: List[Any] = []
    
    def enqueue(self, item: Any):
        """入队"""
        self.items.append(item)
    
    def dequeue(self) -> Any:
        """出队"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """获取队列大小"""
        return len(self.items)


class MinHeap:
    """最小堆"""
    
    def __init__(self):
        self.heap: List[Any] = []
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def left_child(self, i: int) -> int:
        return 2 * i + 1
    
    def right_child(self, i: int) -> int:
        return 2 * i + 2
    
    def insert(self, key: Any):
        """插入元素"""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i: int):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)
    
    def extract_min(self) -> Any:
        """提取最小元素"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if len(self.heap) > 0:
            self._heapify_down(0)
        
        return min_val
    
    def _heapify_down(self, i: int):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._heapify_down(min_index)


__all__ = [
    "Node",
    "LinkedList",
    "TreeNode",
    "BinarySearchTree",
    "Stack",
    "Queue",
    "MinHeap",
]
