def main():
    spacecraft = {
        "name": "James Webb Space Telescope",
        # "distance": "163" 
    }

    spacecraft.update({
        "distance": 0.01,
        "orbit": "Sun"
    })

    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========== REPORT =========

    Name: {spacecraft.get("name", "Unkonw")}
    Distance: {spacecraft.get("distance", "Unkonw")} AU
    orbit: {spacecraft.get("orbit", "Unknow")}

    ===========================
    """

main()