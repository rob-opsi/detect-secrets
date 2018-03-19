from collections import namedtuple


RepoConfig = namedtuple(
    'RepoConfig',
    [
        'base_tmp_dir',
        'baseline',
        'file_exclude_regex',
    ]
)
