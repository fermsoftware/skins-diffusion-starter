
from skins_diffusion import AssetRef

"""
AssetRef(path, id)

Load an AssetRef resource from an explicit file path.

The first argument is the path to the resource file, and the second
argument is the asset ID to modify within that resource.

Example:
    asr = AssetRef("./Resources/AssetRefs/Hero/150_AssetRef.bytes", 15009)

For convenience, AssetRef also supports initializing from a list of
asset IDs. In this form, the required resources are located automatically
under the "Resources" directory.

Example:
    asr = AssetRef([14111, 15009])

This form is intended for workflows that modify multiple assets without
requiring the caller to specify each resource file path manually.

After initialization, call modify() to apply the modifications and save
the resulting files.

    asr.modify()

By default, the output is saved to the current working directory. An
optional output directory can be supplied to save the resulting files
elsewhere.

    asr.modify("output")

Details: The automatic resource lookup relies on the expected directory
structure under "Resources". Ensure that the required resource files are
available before initializing AssetRef.
"""

ast = AssetRef("./Resources/AssetRefs/Hero/150_AssetRef.bytes", 15009)
ast.modify("output")