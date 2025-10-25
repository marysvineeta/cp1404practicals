COLOUR_CODES = {
    "Asparagus": "#87a96b",
    "Aureolin": "#fdee00",
    "Azure1": "#f0ffff",
    "Azure4": "#838b8b",
    "Baby Pink": "#f4c2c2",
    "Baker-Miller Pink": "#ff91af",
    "Banana Mania": "#fae7b5",
    "Barn Red": "#7c0a02",
    "Battleship Gray": "#848482",
    "Beaver": "#9f8170"
}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
