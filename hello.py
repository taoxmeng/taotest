nodes = {'A': ['C', 'E', 'B', 'X'],
         'B': ['C', 'D'],
         'C': ['D','T','R'],
         'D': ['F'],
         'F': ['G','H']
         }

def find_dependencies(target, dependencies):
        dependencies = dependencies + [target]
        if target not in nodes.keys():
            return dependencies
        for node in nodes[target]:
            if node not in dependencies:
                newdependencies = find_dependencies(node, dependencies)
                for node in newdependencies:
                    if node not in dependencies: 
                        dependencies = dependencies + [node]
        return dependencies


print (find_dependencies('A',[]))