with open('log.txt', 'r') as data:
    
    freq = {}

    for datum in data:
        i = int(datum)
        
        if i not in freq.keys():
            freq[i] = 0
        freq[i] += 1
    
    for key in sorted(freq.keys()):
        print('{}\t{}'.format(key, freq[key]))
        
