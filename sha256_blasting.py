from hashlib import sha256

possible_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "0123456789"
tail = "DEHNCHyUEO8kVZBT"
result = "3354de5346a962dd0f344de80cd3c8e5c2d3ce1a18437141b6a645df9b357c91"

for a in possible_str:
    for b in possible_str:
        for c in possible_str:
            for d in possible_str:
                blast_str = a+b+c+d+tail
                if sha256(blast_str.encode()).hexdigest() == result:
                    print(blast_str)
