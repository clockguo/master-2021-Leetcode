def calcEquation(equations,values,queries):
    visited = {}
    graph = {}
    for edge,val in zip(equations,values):
        if edge[0] not in graph:
            graph[edge[0]] = {edge[1]:val}
        else:
            graph[edge[0]][edge[1]]  = val
        if edge[1] not in graph:
            graph[edge[1]] = {edge[0]:1.0/val}
        else:
            graph[edge[1]][edge[0]] = 1.0/val
        visited[edge[0]] = visited[edge[1]] = False
    print(graph)
    # def BFS(nums,ans):
    #     if nums[0] not in graph or nums [1] not in graph:
    #         return None
    #     if nums[0] == nums[1]:
    #         return  ans
    #     for key,value1 in graph[nums[0]].items():
    #         if not visited[key]:
    #             visited[key] = True
    #             tem = BFS([key,nums[1]],ans*value1)
    #             if tem is not None:
    #                 visited[key] = False
    #                 return tem
    #             visited[key] = False
    #     return  None

    def BFS(nums):

        if nums[0] not in graph or nums [1] not in graph:
            return -1.0
        if nums[0] == nums[1]:
            return 1.0
        for key,value1 in graph[nums[0]].items():
            if not visited[key]:
                visited[key] = True
                tem = BFS([key,nums[1]])
                visited[key] = False
                if tem >-1:
                    return  tem*value1
        return -1.0
    res = []
    for query in  queries:
        # tem = BFS(query,1.0)
        # if tem is None:
        #     res.append(-1.0)
        # else:
        #     res.append(tem)
        res.append(BFS(query))
    return  res
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0,3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

print(calcEquation(equations,values,queries))





