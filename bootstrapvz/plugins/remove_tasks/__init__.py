
def resolve_tasks(taskset, manifest):
    # Tasks to be removed are specified in manifest file
    removals = manifest.plugins["remove_tasks"]["tasks"]

    tasksubset = [ task
                    for task in taskset
                    if task.__name__ in removals ]

    for t in tasksubset:
        print("Removing {task} from taskset".format(task=t))
        taskset.discard(t)
