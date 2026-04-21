from museum.artists import get_artist
from museum.artworks import get_artwork

def main():
    user_input = input("Artwork: ")
    # artist = get_artist(query=user_input, limit=3)
    artworks = get_artwork(query=user_input, limit=3)
    for artwork in artworks:
        print(f"[*] {artwork}")

main()