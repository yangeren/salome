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

p = yaml.load(file('keyword.yml'))
a = p['soft']
print a
print a.items()
for x,y in a.items():
    print x,y