from django.db import migrations


def create_posts(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    Post.objects.bulk_create(
        [
            Post(text="Merhaba, bu ilk örnek mesaj."),
            Post(text="Django ile basit bir mesaj panosu."),
            Post(text="Üçüncü mesaj da burada görünecek."),
        ]
    )


def delete_posts(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    Post.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_posts, delete_posts),
    ]
