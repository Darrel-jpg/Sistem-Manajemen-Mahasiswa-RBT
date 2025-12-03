class Node:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, None, None)
        self.NIL.color = "BLACK"
        self.root = self.NIL
    
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def insert(self, nim, nama, jurusan, ipk):
        node = Node(nim, nama, jurusan, ipk)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.nim < x.nim:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y == None:
            self.root = node
        elif node.nim < y.nim:
            y.left = node
        else:
            y.right = node
        
        if node.parent == None:
            node.color = "BLACK"
            return
        
        if node.parent.parent == None:
            return
        
        self.fix_insert(node)
    
    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"
    
    def search(self, nim, node=None):
        if node is None:
            node = self.root
        
        if node == self.NIL or nim == node.nim:
            return node
        
        if nim < node.nim:
            return self.search(nim, node.left)
        return self.search(nim, node.right)
    
    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def delete_node(self, nim):
        z = self.search(nim)
        if z == self.NIL:
            return False
        
        y = z
        y_original_color = y.color
        
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == "BLACK":
            self.fix_delete(x)
        return True
    
    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.rotate_left(x.parent)
                    s = x.parent.right
                
                if s.left.color == "BLACK" and s.right.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.right.color == "BLACK":
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.rotate_right(s)
                        s = x.parent.right
                    
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.rotate_right(x.parent)
                    s = x.parent.left
                
                if s.right.color == "BLACK" and s.left.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.left.color == "BLACK":
                        s.right.color = "BLACK"
                        s.color = "RED"
                        self.rotate_left(s)
                        s = x.parent.left
                    
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.left.color = "BLACK"
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = "BLACK"
    
    def inorder_traversal(self, node, result):
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append(node)
            self.inorder_traversal(node.right, result)
    
    def get_all_students(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result