from django.db import migrations


def correct_demo_movie(apps, schema_editor):
    Movie = apps.get_model('bookings', 'Movie')
    # Match only the original demo data, preserving IDs and related bookings.
    Movie.objects.using(schema_editor.connection.alias).filter(
        title__in=['Inception', 'Nightmare before Christmas', 'The Nightmare Before Christmas'],
        description='A thief who steals secrets through dreams is given a final mission.',
        release_date='2010-07-16',
        duration=148,
    ).update(
        title='The Nightmare Before Christmas',
        description='Jack Skellington, the Pumpkin King of Halloween Town, discovers Christmas Town and tries to take over Christmas.',
        release_date='1993-10-13',
        duration=76,
    )


class Migration(migrations.Migration):
    dependencies = [('bookings', '0001_initial')]

    operations = [
        migrations.RunPython(correct_demo_movie, migrations.RunPython.noop),
    ]
