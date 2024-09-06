def scrape_ufu():
  doc = requests.get("http://www.ufu.br/")
  soup = BeautifulSoup(doc.text, "html.parser")
  links = soup.find("aside").find("ul", "menu").find_all("a")

  with Session(engine) as db:
    db.query(model.ScrappedText).delete()
    db.commit()

  with Session(engine) as db:
    for l in links:
      db.add(model.ScrappedText(menuNav=l.text, link=l.get('href')) )
    
    db.commit()