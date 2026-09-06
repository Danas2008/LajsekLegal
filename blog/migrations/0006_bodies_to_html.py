from django.db import migrations
from django.utils.html import escape


def to_html(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    for post in BlogPost.objects.all():
        if '<' in post.body:
            continue  # already HTML (edited via the rich text editor)
        paragraphs = [p.strip() for p in post.body.split('\n\n') if p.strip()]
        post.body = ''.join(f'<p>{escape(p)}</p>' for p in paragraphs)
        post.save(update_fields=['body'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_update_telefonaty_body'),
    ]

    operations = [
        migrations.RunPython(to_html, noop),
    ]
