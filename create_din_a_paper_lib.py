import json
import math

DIGITS = 1

A0_AREA = 1e6  # mm

paperdict = {}

# DIN A0 - DIN A6
# all pages calculated in portrait orientation
for i in range(0, 7):
    area_i = A0_AREA * (0.5**i)

    width_i = math.sqrt(area_i / math.sqrt(2))
    height_i = area_i / width_i

    paperdict["a" + str(i) + "paper"] = {
        "portrait": {
            "height": round(height_i, DIGITS),
            "width": round(width_i, DIGITS),
        },
        "landscape": {
            "height": round(width_i, DIGITS),
            "width": round(height_i, DIGITS),
        },
        "area": area_i
    }

paperdict_json = json.dumps(paperdict, indent=4)

with open("templates/paperlib.json", "w") as paperlibfile:
    paperlibfile.write(paperdict_json)
