def histogram(znaki):
    d = dict()
    for l in znaki:
        d[l] = znaki.count(l)
    return d

print(histogram("mam cos w nosie "))
    
