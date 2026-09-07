from django.db import migrations

FAQS = [
    {
        'order': 1,
        'question': 'Jak probíhá první konzultace?',
        'answer': 'Nejlépe mě kontaktujte e-mailem na vlajsek@lajseklegal.cz s popisem Vašeho případu. Do dvou dnů se ozvu a domluvíme si osobní nebo online schůzku.',
    },
    {
        'order': 2,
        'question': 'Kolik stojí právní služby?',
        'answer': 'Nejčastěji účtuji hodinovou sazbou cca 3 000 Kč/hod podle náročnosti případu. Přesnou cenu vždy sdělím předem k odsouhlasení. Více na stránce Odměna.',
    },
    {
        'order': 3,
        'question': 'Poskytujete i mediaci místo soudního sporu?',
        'answer': 'Ano, jsem akreditovaným mediátorem. Tam, kde je reálná šance na dohodu, nabízím mimosoudní řešení formou mediace, které bývá rychlejší a levnější než soudní spor.',
    },
    {
        'order': 4,
        'question': 'Je konzultace přes e-mail nebo telefon možná?',
        'answer': 'Ano, konzultace probíhají osobně v kanceláři, telefonicky i online – podle toho, co Vám nejlépe vyhovuje.',
    },
    {
        'order': 5,
        'question': 'Jak si mohu rezervovat schůzku?',
        'answer': 'Přes stránku Rezervace schůzky si vyberete volný termín a vyplníte krátký formulář. Rezervaci Vám poté potvrdíme e-mailem.',
    },
]


def add_faqs(apps, schema_editor):
    FAQ = apps.get_model('engagement', 'FAQ')
    for item in FAQS:
        FAQ.objects.get_or_create(question=item['question'], defaults=item)


def remove_faqs(apps, schema_editor):
    FAQ = apps.get_model('engagement', 'FAQ')
    FAQ.objects.filter(question__in=[f['question'] for f in FAQS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('engagement', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_faqs, remove_faqs),
    ]
