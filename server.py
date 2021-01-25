from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/")
def index():
  with open('.data/places.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    for row in data:
      if not first_line:
        places.append({
          "name": row[0],
          "review": row[1],
          "pro": row[2]
        })
      else:
        first_line = False
  return render_template("index.html", places=places)

@app.route("/submit", methods=["GET", "POST"])
def submit():
  if request.method == "GET":
    return redirect(url_for('index'))
  elif request.method == "POST":
    userdata = dict(request.form)
    name = userdata["name"][0]
    review = userdata["review"][0]
    product = userdata["pro"][0]
    # if len(name) < 2 and len(review) < 3 and (len(product) < 10 or "png" not in product):
    #   return "Please submit valid data."
    with open('.data/places.csv', mode='a') as csv_file:
      data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data.writerow([name, review, product])
  return render_template("submit.html")

if __name__ == "__main__":
  app.run(debug=True)
