import datetime

def naming_func(naming_option):
    if naming_option != "0":
        return naming_option
    else:
        today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"_backup_{today}"
