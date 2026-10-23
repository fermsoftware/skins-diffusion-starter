
from skins_diffusion import Databin

"""
Databin(path, tasks)

Load a Databin resource from an explicit file path and configure the
tasks to perform on the resource.

The first argument is the path to the Databin file. The second argument
specifies the character or skin IDs to process.

Databin supports three task formats:
    - A single integer ID, for one task.
    - A list of integer IDs, for multiple tasks using the default
      source-ID derivation rule.
    - A list of (from_id, to_id) pairs, for explicit task mappings.

For a single task, pass the target ID directly.

    db = Databin("./Resources/Databin/Client/Actor/heroSkin.bytes", 15009)

For multiple tasks, pass a list of target IDs.

    db = Databin("./Resources/Databin/Client/Actor/heroSkin.bytes", [14111, 15009])

In this form, each ID is interpreted as a target ID, and the
corresponding source ID is derived automatically according to the
default mapping rule.

For greater control, provide explicit source-to-target mappings.

    db = Databin(
        "./Resources/Databin/Client/Actor/heroSkin.bytes",
        [
            (14102, 14111),
            (15001, 15009),
        ],
    )

Each pair specifies the source ID and the target ID for a task.

The resource path can also be omitted when the required resources
should be resolved automatically from the "Resources" directory.

    db = Databin([14111, 15009])

This form supports multiple tasks using the default source-ID
derivation rule. Explicit mappings can also be supplied.

    db = Databin([
        (14102, 14111),
        (15001, 15009),
    ])

When the path is omitted, Databin is responsible for locating the
required resource files under "Resources". The expected directory
structure and resource files must be available for automatic
resolution to succeed.

Details: The explicit-path forms operate on the specified Databin
file, while the automatic-resolution forms locate resources based on
the supplied task IDs and the package's resource-resolution rules.

The integer-ID forms rely on the default source-ID derivation rule.
The pair form allows the source and target IDs to be specified
independently for each task.
"""

d = Databin([14111, 15009])
d.modify("output")