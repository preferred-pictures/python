# PreferredPictures Python Client Library

The [PreferredPictures](https://preferred.pictures) Python library provides a convenient way to call the
[PreferredPictures](https://preferred.pictures) API for applications written in Python.

[View the documentation of this module](https://preferred-pictures.github.io/python/build/html/index.html)

[View the documentation about the PreferredPicture's API](https://docs.preferred.pictures/api-sdks/api)

[Learn more about what PreferredPictures can do.](https://docs.preferred.pictures/)

## Installation

```
$ pip install preferred_pictures
```

## Usage

The package needs to be configured with your account's identity and
secret key, which is available in the PreferredPictures interface.

```python

from preferred_pictures import Client

pp = Client("testidentity", "secret123456")
url = pp.create_choose_url(
    choices=[
        "https://example.com/image-red.jpg",
        "https://example.com/image-green.jpg",
        "https://example.com/image-blue.jpg"
    ],
    tournament="test-tournament")

# Or more using a prefix and suffix for choices

url = pp.create_choose_url(
    choices=["red", "green", "blue"],
    choices_prefix="https://example.com/image-",
    choices_suffix=".jpg",
    tournament="test-tournament")


# The URL returned will appear to be something like:
#
# https://api.preferred-pictures.com/choose-url?choices%5B%5D=red&choices%5B%5D=green&choices%5B%5D=blue&tournament=test-tournament&expiration=1597011644&uid=362511d6-997f-452b-afee-8e46331da04a&ttl=600&identity=testidentity&signature=7c6d305405b4518876543435ce5657ee820cad0601359fa173a854dc0dfd6ea1
#
```

## License

This client uses the MIT license.
