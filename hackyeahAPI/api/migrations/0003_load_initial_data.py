from django.db import migrations
from django.core.management import call_command
import os

# Correctly locate the fixtures directory relative to this migration file
fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'
fixture_path = os.path.join(fixture_dir, fixture_filename)

def load_fixture(apps, schema_editor):
    """Loads the initial_data.json fixture."""
    # Ensure the fixture file exists before trying to load it
    if not os.path.exists(fixture_path):
        raise FileNotFoundError(f"Fixture file not found at {fixture_path}")
    
    print(f"Loading fixture from: {fixture_path}")
    call_command('loaddata', fixture_path)

def unload_fixture(apps, schema_editor):
    """Deletes all data from the relevant models to reverse the migration."""
    # Using model names as strings to avoid potential import issues
    models_to_clear = [
        "Impact", "Condition", "Answer", "EducationalContent", 
        "Question", "Challenge", "LifeStage", "Attribute"
    ]
    for model_name in models_to_clear:
        Model = apps.get_model('api', model_name)
        Model.objects.all().delete()
    print("Reversed data migration by deleting all content from specified models.")


class Migration(migrations.Migration):

    dependencies = [
        # This should be the name of your last 'regular' migration
        ('api', '0002_challenge_educationalcontent'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]