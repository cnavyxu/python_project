# 数据结构教程

本教程介绍如何使用项目中实现的各种数据结构。

## 链表

### 单向链表

```python
from src.data_structures import LinkedList

# 创建链表
ll = LinkedList()

# 添加元素
ll.append(1)
ll.append(2)
ll.append(3)

# 在开头添加
ll.prepend(0)

# 删除元素
ll.delete(2)

# 转换为列表
print(ll.to_list())  # [0, 1, 3]
```

## 树

### 二叉搜索树

```python
from src.data_structures import BinarySearchTree

# 创建树
bst = BinarySearchTree()

# 插入元素
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)

# 搜索
found = bst.search(7)  # True
not_found = bst.search(6)  # False

# 中序遍历
inorder = bst.inorder_traversal()
print(inorder)  # [1, 3, 5, 7, 9]
```

## 栈

```python
from src.data_structures import Stack

# 创建栈
stack = Stack()

# 入栈
stack.push(1)
stack.push(2)
stack.push(3)

# 出栈
top = stack.pop()  # 3

# 查看栈顶
peek = stack.peek()  # 2

# 检查是否为空
is_empty = stack.is_empty()  # False

# 获取大小
size = stack.size()  # 2
```

## 队列

```python
from src.data_structures import Queue

# 创建队列
queue = Queue()

# 入队
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# 出队
first = queue.dequeue()  # 1

# 检查是否为空
is_empty = queue.is_empty()  # False

# 获取大小
size = queue.size()  # 2
```

## 堆

### 最小堆

```python
from src.data_structures import MinHeap

# 创建最小堆
heap = MinHeap()

# 插入元素
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)

# 提取最小元素
min_val = heap.extract_min()  # 1
next_min = heap.extract_min()  # 3
```

## 实际应用示例

### 使用栈实现括号匹配

```python
from src.data_structures import Stack

def is_balanced(expression):
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs.keys():
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()

# 测试
print(is_balanced("()[]{}"))  # True
print(is_balanced("([)]"))    # False
```

### 使用队列实现BFS

```python
from src.data_structures import Queue

def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.enqueue(start)
    result = []
    
    while not queue.is_empty():
        node = queue.dequeue()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                queue.enqueue(neighbor)
    
    return result

# 测试
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

print(bfs(graph, 0))  # [0, 1, 2, 3, 4, 5]
```
