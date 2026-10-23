
from skins_diffusion import PrefabCharacter

"""
PrefabCharacter(path, id)

Load a PrefabCharacter resource from an explicit file path.

The first argument is the path to the resource file, and the second
argument is the asset ID used to identify the character to modify.

Example:
    p = PrefabCharacter("./Resources/Prefab_Characters/Actor_141_Infos.pkg.bytes", 14111)

For modifying multiple characters, PrefabCharacter also accepts a list
of asset IDs. In this form, the required resources are located
automatically under the "Resources" directory.

    p = PrefabCharacter([14111, 15009])

When a list of asset IDs is supplied, each ID is interpreted as a
target character ID. The corresponding source character ID is derived
by replacing the skin-specific portion of the ID with 00.

For example, the mapping is equivalent to:

    (14100, 14111)
    (15000, 15009)

This default mapping is intended for modifying a character's skin
while retaining the corresponding base character.

For more control, a list of explicit (from_id, to_id) pairs can
be supplied instead.

    p = PrefabCharacter([
        (14102, 14111),
        (15001, 15009),
    ])

Each pair identifies the source character and the target character
whose data is used for the modification.

In the example above:
    (14101, 14111)  modifies Luariel Black Wing (14101) to Lauriel Dimension
                    Breaker (14111).

    (15001, 15009)  modifies Nakroth Demonic (15001) to Nakroth Dimension
                    Breaker (15009).

Details: The automatic resource lookup relies on the expected directory
structure under "Resources". Ensure that the required resource files
are available before initializing PrefabCharacter.

The list-of-IDs form uses the default source-ID derivation rule, whereas
the list-of-pairs form allows each source and target ID to be specified
explicitly.
"""

p = PrefabCharacter("./Resources/AssetRefs/Hero/Actor_141_Infos.pkg.bytes", 14111)
p.modify("output")