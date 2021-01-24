import os
# from pathlib import Path

from psd_tools import PSDImage


script_p = os.path.dirname(__file__)
rel_p = "data/Marketing-Growth.psd"
abs_file_p = os.path.join(script_p, rel_p)

print(script_p)
print(abs_file_p)


# psd = PSDImage.open('Marketing-Growth.psd')
# psd.composite().save('Marketing-Growth.png')

# for layer in psd:
#     print(layer)
#     image = layer.composite()