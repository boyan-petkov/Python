
# Create a class called PhotoAlbum. Upon initialization it should receive pages (int). It should also have one more attribute: 
#   photos (empty matrix) representing the album with its pages where you should put the photos. Each page can contain only 4 photos. 
#   The class should also have 3 more methods:
# •	from_photos_count(photos_count: int) – creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos.
# •	add_photo(label:str) – adds the photo in the first possible page and slot and return 
# "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}". If there are no free slots left, 
# return "No more free slots"
# •	display() – returns a string representation of each page and the photos in it. 
# Each photo is marked with "[]" and the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
# -----------
# [] []
# -----------
# and if we have 2 empty pages:
# -----------

# -----------

# -----------

class PhotoAlbum:

    __PAGE_CAPACITY = 4

    def __init__(self, pages: int) -> None:
        self.photos = [[] for _ in range(pages)]
        self.pages = pages

    @classmethod
    def from_photos_count(cls, photos_count: int) -> int:
        pages = photos_count // PhotoAlbum.__PAGE_CAPACITY
        pages += min(1, photos_count % PhotoAlbum.__PAGE_CAPACITY)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        try:
            free_page = self.__find_free_page()
            self.photos[free_page].append(label)
            used_slots = len(self.photos[free_page])
            return f"{label} photo added successfully on page {free_page + 1} slot {used_slots}"
        except TypeError:
            return "No more free slots"

    def display(self) -> str:
        retval = '-' * 11
        for page in self.photos:
            retval += '\n' + str('[] ' * len(page)).rstrip() + '\n' + '-' * 11
        return retval

    def __find_free_page(self):
        try:
            return next(i for i, page in enumerate(self.photos) if len(page) < PhotoAlbum.__PAGE_CAPACITY)
        except StopIteration:
            return


if __name__ == '__main__':
    album = PhotoAlbum(2)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())
