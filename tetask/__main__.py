from threading import Thread
import time

# A node can either be:
# - a task;
# - a group of nodes which executes sequentially in order;
# - a group of nodes which executes in parallel.
task_graph = {
    "name": "S1",
    "type": "sequence",
    "children": [
        {
            "name": "P1",
            "type": "parallel",
            "children": [
                {
                    "name": "T1",
                    "type": "task",
                    "duration": 5,
                },
                {
                    "name": "T2",
                    "type": "task",
                    "duration": 2,
                },
            ],
        },
        {
            "name": "T3",
            "type": "task",
            "duration": 3,
        },
    ],
}


def execute_node(node):
    if node['type'] == 'task':
        print('Starting task %s...' % node['name'])
        time.sleep(node['duration'])
        print('Task %s done.' % node['name'])

    elif node['type'] == 'sequence':
        for child_node in node['children']:
            execute_node(child_node)

    elif node['type'] == 'parallel':
        threads = [Thread(target=execute_node, args=(child_node,))
                   for child_node in node['children']]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


execute_node(task_graph)
