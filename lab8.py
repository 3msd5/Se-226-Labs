class ArchiveItem:
    def __init__(self, uid: str, title: str, year: int):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArchiveItem):
            return NotImplemented
        return self.uid == other.uid

    def is_recent(self, n: int) -> bool:
        return self.year >= 2025 - n


######################2##############################
class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        base = super().__str__()
        return f"Book -> {base}, Author: {self.author}, Pages: {self.pages}"


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid,title,year)
        self.journal = journal
        self.doi = doi

    def __str__(self)->str:
        base = super().__str__()
        return (f"Article -> {base}, Journal: {self.journal}, DOI: {self.doi}")

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid,title,year)
        self.host = host
        self.duration = duration

    def __str__(self)->str:
        base = super().__str__()
        return f"Podcast -> {base}, Host: {self.host}, Duration: {self.duration}"


######################3##############################

def save_to_file(items: list[ArchiveItem], filename:str):
    with open(filename,'w', encoding='utf-8') as f:
        for item in items:
            if isinstance(item, Book):
                line = f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n"
            elif isinstance(item, Article):
                line = f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n"
            elif isinstance(item, Podcast):
                line = f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n"
            else:
                continue
            f.write(line)


######################4##############################

def load_from_file(filename: str) -> list[ArchiveItem]:
    items: list[ArchiveItem] = []
    with open(filename, 'r', encoding='utf-8') as f:
        for raw in f:
            parts = raw.strip().split(',')
            kind = parts[0]
            if kind == 'Book':
                _, uid, title, year, author, pages = parts
                items.append(Book(uid, title, int(year), author, int(pages)))
            elif kind == 'Article':
                _, uid, title, year, journal, doi = parts
                items.append(Article(uid, title, int(year), journal, doi))
            elif kind == 'Podcast':
                _, uid, title, year, host, duration = parts
                items.append(Podcast(uid, title, int(year), host, int(duration)))
    return items

######################5.a##############################

if __name__ == "__main__":
    archive_items = [
        Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
        Book("B002", "Python Tricks", 2024, "Dan Bader", 250),
        Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
        Article("A102", "AI Ethics", 2025, "Science", "10.5678/ethics123"),
        Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
        Podcast("P302", "CodeLife", 2021, "John Smith", 60),
    ]

######################5.b##############################
save_to_file(archive_items, "archive.txt")

######################5.c##############################
loaded_items = load_from_file("archive.txt")

######################5.d##############################
print("All Archive Items:")
for item in loaded_items:
    print(item)

######################6.a##############################
print("\nRecent Items (<=5 years old):")
for item in archive_items:
    if item.is_recent(5):
        print(item)

######################6.b##############################
print("\nArticles with DOI starting '10.1234':")
for item in loaded_items:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)
