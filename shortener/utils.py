import random
import string

# this function generate random character for short url
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=7))


# this function check if the short url is already exists in database
# if exists, it will generate new one
def create_short_url(instance):
    new_url = generate_short_url()
    url_exists = instance.__class__.objects.filter(short_url=new_url).exists()
    if url_exists:
        return create_short_url(instance)
    return new_url