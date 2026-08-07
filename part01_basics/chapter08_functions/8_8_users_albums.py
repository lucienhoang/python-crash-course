def make_album(artis_name, album_title):
    """Return a dictionary of information about album"""
    album = {"artist": artis_name, "title": album_title}
    return album


prompt_artist = "Enter an album's artist: "
prompt_title = "Enter an album's title: "


while True:
    print("\nEnter album information (artist & title)")
    print("(Enter 'q' to quit)")

    artist = input(prompt_artist)
    if artist == "q":
        break

    title = input(prompt_title)
    if title == "q":
        break

    album = make_album(artist, title)

    print(f"\n{album}")

# Enter album information (artist & title)
# (Enter 'q' to quit)
# Enter an album's artist: Luci
# Enter an album's title: Pray Lord

# {'artist': 'Luci', 'title': 'Pray Lord'}

# Enter album information (artist & title)
# (Enter 'q' to quit)
# Enter an album's artist: Khoa
# Enter an album's title: Life is Beautyful

# {'artist': 'Khoa', 'title': 'Life is Beautyful'}

# Enter album information (artist & title)
# (Enter 'q' to quit)
# Enter an album's artist: q
