COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

def main():
    color_name = input("Enter color name: ").lower()
    while color_name != "":
        try:
            print(f"{color_name.title()} has the hex code {COLOR_TO_HEX[color_name.title()]}")
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter color name: ").lower()

if __name__ == "__main__":
    main()
