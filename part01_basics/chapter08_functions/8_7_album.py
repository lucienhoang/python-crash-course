def make_album(artis_name, album_title, number_of_tracks=""):
    """Return a dictionary of information about album"""
    if number_of_tracks:
        album = {
            "artis": artis_name,
            "title": album_title,
            "number_of_tracks": number_of_tracks,
        }
    else:
        album = {"artis": artis_name, "title": album_title}
    return album


lucien_album = make_album("luci", "Praise the Lord")
print(lucien_album)
# {'artis': 'luci', 'title': 'Praise the Lord'}

lucien_album = make_album("khoa", "Jesus is King")
print(lucien_album)
# {'artis': 'khoa', 'title': 'Jesus is King'}

lucien_album = make_album("lucien", "I keeping my faith on you, dear Lord", 7)
print(lucien_album)
# {'artis': 'lucien', 'title': 'I keeping my faith on you, dear Lord', 'number_of_tracks': 7}
