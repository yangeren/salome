#*--coding:utf-8--*
__author__ = 'yer'
import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
print yaml.dump(yaml.load(document))