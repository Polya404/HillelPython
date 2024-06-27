total_seconds = int(input("Enter total_seconds: "))

SECONDS_IN_A_DAY = 86400
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MINUTE = 60

endings_dict = {
    "день": ["день", "дні", "днів"]
}

if 0 <= total_seconds < 8640000:
    days, total_seconds = divmod(total_seconds, SECONDS_IN_A_DAY)
    hours, total_seconds = divmod(total_seconds, SECONDS_IN_AN_HOUR)
    minutes, seconds = divmod(total_seconds, SECONDS_IN_A_MINUTE)

    if 11 <= days <= 19:
        days_str = endings_dict["день"].pop(2)
    else:
        last_digit = days % 10
        days_str = (endings_dict["день"][0] if last_digit == 1 else
                    endings_dict["день"][1] if 2 <= last_digit <= 4 else
                    endings_dict["день"][2])

    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(f"{days} {days_str}, {time_str}")
else:
    print("Total seconds must be between 0 and 8639999.")
