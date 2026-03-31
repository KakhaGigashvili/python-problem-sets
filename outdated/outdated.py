while True:
    date = input("Date: ").strip()

    months = [
        "January",
        "February", 
        "March", 
        "April",
        "May", 
        "June", 
        "July", 
        "August",
        "September", 
        "October", 
        "November", 
        "December"
    ]

    try:
        if "/" in date:
            month, day, year = date.split("/")

        else:
            if "," not in date:
                continue

            date = date.replace(",", "")
            month_name, day, year = date.split()

            if month_name not in months:
                continue

            month = months.index(month_name) + 1

        month = int(month)
        day = int(day)
        year = int(year)

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

    except ValueError:
        continue