from models.band import Band


def test_do_it_work():
    band_dict = {
        "name": "name",
        "songs_played": ["first song", "second song"]
    }
    band = Band(**band_dict)
    assert type(band) == Band