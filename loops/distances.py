distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "pioneer 10": 80,
    "New horizons": 58,
    "pioneer 11": 44,  
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} km")

def convert(au):
    return f"{au * 150_000_000:,}"

main()