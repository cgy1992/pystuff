So, for now I can't properly manage the category for small notes. So I've called that folder `random`. May be in the future I'll move some stuff to proper sections. And there will be some plain text may be split in paragraphs.

It is gonna be here some thoughts about py or about learning.

### Usage of several context managers simultaneously
```python
with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    for i in (a, b):
        i.write('text')
```
