from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

USER_TYPES = (
    ('Tourist', 'Tourist'),
    ('Business', 'Business'),
    ('Student', 'Student'),
)

DATA_TYPES = (
    ('All Categories', 'All Categories'), # Needed when searching for all entries
    ('College', 'College/Schools'),
    ('Library', 'Library'),
    ('Industry', 'Industry'),
    ('Hotel', 'Hotel'),
    ('Park', 'Park'),
    ('Zoo', 'Zoo'),
    ('Museum', 'Museum'),
    ('Restaurant', 'Restaurant'),
    ('Mall', 'Mall')
)

CITIES = (
    ('All Cities', 'All Cities'), # Needed when searching for all entries
    ('Brisbane', 'Brisbane'),
    ('Sydney', 'Sydney'),
    ('Melbourne', 'Melbourne')
)

STATES = (
    ('All States', 'All States'), # Needed when searching for all entries
    ('QLD', 'QLD'),
    ('NSW', 'NSW'),
    ('VIC', 'VIC'),
    ('ACT', 'ACT'),
    ('TAS', 'TAS'),
    ('SA', 'SA'),
    ('NT', 'NT'),
    ('WA', 'WA')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=15, choices=USER_TYPES)
    is_admin = models.BooleanField()

class Data(models.Model):
    author = models.ForeignKey('auth.User', default="none")
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=200)
    long_description = models.TextField()
    data_type = models.CharField(max_length=100, choices=DATA_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=100, choices=CITIES)
    state = models.CharField(max_length=100, choices=STATES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    link = models.URLField()
    map_link = models.URLField(max_length=1000)
    image_link = models.URLField()

    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)


    # This is for the type specific info like department(s), industry type etc
    def special_default():
        return {"data": "null"}
    special = models.TextField("", default=special_default)

    def edit(self):
        self.edited_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
