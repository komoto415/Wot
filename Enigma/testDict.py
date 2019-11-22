def main():
    dict = { "A":1, "B":2}
    for key, value in dict.items():
        print(key, '->',  value)
        value = dict[key] = key * 2
        print(key, '->', value)
    print(dict)    
main()