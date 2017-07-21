

def validate_manifest(data, validator, error):
    from bootstrapvz.common.tools import rel_path
    validator(data, rel_path(__file__, 'manifest-schema.yml'))


def resolve_tasks(taskset, manifest):
    from tasks import RemoveMirrors
    taskset.add(RemoveMirrors)

# vi: ts=4 expandtab
