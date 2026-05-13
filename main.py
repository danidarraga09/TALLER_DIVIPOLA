from flask import Flask, render_template, jsonify

from files import Files

app = Flask(__name__)

f = Files()

# Leer CSV
multilist = f.read_divipola("DIVIPOLA.csv")

# Mostrar multilista en consola
multilist.print_multilist()


@app.route("/")
def root():

    markers = f.get_markers(multilist)

    return render_template(
        "index.html",
        markers=markers
    )


# API JSON
@app.route("/api/divipola")
def api_divipola():

    markers = f.get_markers(multilist)

    return jsonify(markers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)