
# %% IMPORTS

from invoke import Collection

from . import (
    checks,
    cleans,
    containers,
    docs,
    formats,
    installs,
    mlflows
)

# %% NAMESPACES

ns = Collection()

# %% COLLECTIONS

ns.add_collection(checks)
ns.add_collection(cleans)
ns.add_collection(containers)
ns.add_collection(docs)
ns.add_collection(formats)
ns.add_collection(installs)
ns.add_collection(mlflows)
