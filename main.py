

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return  ("""<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert">
              </form>"""        
               + "Fahrenheit: "
                + fahrenheit)


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""

    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places

    except ValueError:
        return "invalid input, try again, Christina"

    return str(fahrenheit)

# if __name__ == "__main__":
#     celsius = input("Celsius: ")
#     print("Fahrenheit:", fahrenheit_from(celsius))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)