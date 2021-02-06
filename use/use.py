import os

from psd_tools import PSDImage


# file open idiom/pattern
# with open(os.path.normpath('use/data/Marketing-Growth.psd'), 'rb') as f:
#     contents = f.read()
#     print(contents)

psd = PSDImage.open(os.path.normpath('use/data/Marketing-Growth.psd'))
psd.composite().save(os.path.normpath('use/data/Marketing-Growth.png'))

for layer in psd:
    print(layer)
    image = layer.composite()