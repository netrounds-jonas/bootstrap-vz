from bootstrapvz.base import Task
from bootstrapvz.common import phases
from bootstrapvz.base.pkg.sourceslist import Source
from bootstrapvz.common.tasks.apt import AddDefaultSources

from re import match


class RemoveMirrors(Task):
    description = 'Remove specific mirrors'
    phase = phases.preparation
    predecessors = [AddDefaultSources]

    @classmethod
    def run(cls, info):
        from bootstrapvz.common.tools import log_check_call

        source_lists = info.source_lists
        types = dict(
                default='{apt_mirror}\s+{system.release}\s+',
                updates='{apt_mirror}\s+{system.release}-updates\s+',
                security='http://security.debian.org/\s+{system.release}/updates')

        for t in types:
            types[t] = types[t].format(**source_lists.manifest_vars)

        for ignore_str in info.manifest.plugins['remove_updates']['ignore']:
            ops = ignore_str.split(':')
            if len(ops) != 2:
                continue

            search_mirror = '^deb(\-src)?\s+'
            key = ops[0]
            t = ops[1]
            
            if t not in types or key not in source_lists.sources:
                continue

            source_list = source_lists.sources[key]
            search_mirror += types[t]

            i = 0
            while i < len(source_list):
                source = source_list[i]
                if match(search_mirror, str(source)):
                    del source_list[i]
                else:
                    i += 1
            
# vi: ts=4 expandtab
