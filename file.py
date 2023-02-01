def save_to_file(file_name, jobs):
  # w = 쓰기 전용
  file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
  file.write("Company, Position, Location, URL\n")
  
  
  for job in jobs:
    file.write(f"{job['company']},{job['position']},{job['location']},{job['link']}\n")
    
  file.close()
