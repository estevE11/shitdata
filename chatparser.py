id_name = ["roger", "Brrroo", "juke"]
name_id = {
    "roger": 0,
    "Brrroo": 1,
    "juke": 2
}

def parse_chat(path):
    data = open(path).read().split("\n")[8:-1]
    
    count = [5, 6, 5]

    for line in data:
        msg = parse_msg(line)
        count[msg["id_user"]] += 1

    print("Cagades del 11/01 al 16/3:")
    print(" Esteve: " + str(count[0]))
    print(" Raul: " + str(count[1]))
    print(" Lluc: " + str(count[2]))

def parse_msg(line):
    line = line.split(" ")
    
    date = line[0][1:-1]
    time = line[1][:-1]
    name = line[2]
    if name.endswith(":"):
        name = name[:-1]

    msg = {
        "time": time,
        "date": date,
        "id_user": name_id[name]
    }
    return msg

if __name__ == "__main__":
    parse_chat("chat.txt")