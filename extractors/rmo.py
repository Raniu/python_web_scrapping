from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def extract_rmo_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers=headers)
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    
    for job in jobs:
      anchor = job.find("a", class_="preventLink")
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      
      if anchor:
        link = f"https://remoteok.com/{anchor['href']}"
      if company:
        company = company.string.strip().replace(",", "")
      if position:
        position = position.string.strip().replace(",", "")
      if location:
        location = location.string.strip().replace(",", "")

      if link and company and position and location:
        job = {
          'link': link,
          'company': company,
          'position': position,
          'location': location,
        }
        results.append(job)
  else:
    print("Can't get jobs.")
    
  return results

# jobs = extract_jobs("rust")

# print(jobs)
