"""
A package for concise manipulation of VOEvent XML packets.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("voevent-parse")
except PackageNotFoundError:
    # Package is not installed
    __version__ = "unknown"

import voeventparse.definitions as definitions
from voeventparse.convenience import (
    get_event_position,
    get_event_time_as_utc,
    get_grouped_params,
    get_toplevel_params,
    prettystr,
    pull_astro_coords,
    pull_isotime,
    pull_params,
)
from voeventparse.misc import (
    Position2D,
    citation,
    event_ivorn,
    group,
    inference,
    param,
    reference,
)
from voeventparse.voevent import (
    add_citations,
    add_how,
    add_where_when,
    add_why,
    assert_valid_as_v2_0,
    dump,
    dumps,
    load,
    loads,
    set_author,
    set_who,
    valid_as_v2_0,
    voevent,
    voevent_v2_0_schema,
)

__all__ = [
    # Version
    "__version__",
    # Definitions module
    "definitions",
    # Convenience functions
    "get_event_position",
    "get_event_time_as_utc",
    "get_grouped_params",
    "get_toplevel_params",
    "prettystr",
    "pull_astro_coords",
    "pull_isotime",
    "pull_params",
    # Misc classes and functions
    "Position2D",
    "citation",
    "event_ivorn",
    "group",
    "inference",
    "param",
    "reference",
    # VOEvent functions
    "add_citations",
    "add_how",
    "add_where_when",
    "add_why",
    "assert_valid_as_v2_0",
    "dump",
    "dumps",
    "load",
    "loads",
    "set_author",
    "set_who",
    "valid_as_v2_0",
    "voevent",
    "voevent_v2_0_schema",
]
