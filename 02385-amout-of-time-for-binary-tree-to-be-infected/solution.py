class Solution:
    def amountOfTime(self, root, start):
        
        # Step 1: Store parent of every node
        parent = {}
        
        def dfs(node, par=None):
            if not node:
                return
            
            parent[node] = par
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        
        # Step 2: Find the starting node
        start_node = None
        
        for node in parent:
            if node.val == start:
                start_node = node
                break
        
        # Step 3: BFS infection
        queue = deque([start_node])
        visited = {start_node}
        time = 0
        
        while queue:
            size = len(queue)
            infected_new = False
            
            for _ in range(size):
                node = queue.popleft()
                
                # Left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                    infected_new = True
                
                # Right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                    infected_new = True
                
                # Parent
                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])
                    infected_new = True
            
            if infected_new:
                time += 1
        
        return time
        