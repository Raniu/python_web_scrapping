from flask import Flask, render_template, request, redirect, send_file
from extractors.rmo import extract_rmo_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else:
    rmo = extract_rmo_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = rmo + wwr
    db[keyword] = jobs
    jobs_length = len(jobs)
  return render_template("search.html", keyword=keyword, jobs=jobs, jobs_length=jobs_length)

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)

  
app.run("0.0.0.0")