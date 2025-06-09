#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import yaml
import sys

def etree_to_dict(elem):
    d = {}
    if elem.attrib:
        d.update({f"@{k}": v for k, v in elem.attrib.items()})
    children = list(elem)
    if children:
        child_dict = {}
        for child in children:
            child_result = etree_to_dict(child)
            tag = child.tag
            if tag not in child_dict:
                child_dict[tag] = []
            child_dict[tag].append(child_result)
        for k, v in child_dict.items():
            d[k] = v[0] if len(v) == 1 else v
    elif elem.text and elem.text.strip():
        d["#text"] = elem.text.strip()
    return d

if len(sys.argv) != 3:
    print("Uso: xml_to_yaml.py <input.xml> <output.yml>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

tree = ET.parse(input_file)
root = tree.getroot()
data = {root.tag: etree_to_dict(root)}

with open(output_file, "w") as f:
    yaml.dump(data, f, default_flow_style=False)
