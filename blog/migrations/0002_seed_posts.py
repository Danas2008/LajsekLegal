from django.db import migrations

POSTS = [
    {
        'slug': 'chat-control-ochrana-deti-nebo-digitalni-kontrola',
        'title': 'Chat Control: ochrana dětí, nebo začátek nové éry digitální kontroly?',
        'published_at': '2026-07-13',
        'excerpt': 'Co navrhovaná regulace plošné kontroly komunikace přinese uživatelům a jaká jsou rizika z pohledu ochrany soukromí.',
        'body': (
            'Evropská legislativa známá jako „Chat Control“ má za cíl bojovat proti šíření '
            'závadného obsahu v komunikačních službách. Otevírá ale zásadní otázky ohledně '
            'ochrany soukromí a důvěrnosti komunikace běžných uživatelů.\n\n'
            'V tomto článku se podíváme na to, co návrh v praxi znamená, koho se dotkne a '
            'jaké kroky mohou jednotlivci i firmy podniknout k ochraně svých práv.'
        ),
    },
    {
        'slug': 'co-je-a-co-neni-bezne-opotrebeni',
        'title': 'Co je a co není běžné opotřebení? Prakticky a srozumitelně',
        'published_at': '2026-06-25',
        'excerpt': 'Spory o vrácení kauce kvůli opotřebení bytu patří k nejčastějším. Jak se v tom vyznat?',
        'body': (
            'Při skončení nájmu často dochází ke sporům o to, co je běžné opotřebení bytu a co '
            'už jde nad jeho rámec. Zákon zde nedává úplně jasný návod, proto je potřeba vycházet '
            'z judikatury a zvyklostí.\n\n'
            'V článku vysvětlujeme, jak se opotřebení posuzuje, na co si dát pozor při přebírání '
            'a předávání bytu, a jak postupovat, pokud se s pronajímatelem nemůžete dohodnout.'
        ),
    },
    {
        'slug': 'otravne-reklamni-telefonaty-co-delat',
        'title': 'Otravné reklamní telefonáty: co dělat, když vám firma volá bez vyžádání',
        'published_at': '2026-06-14',
        'excerpt': 'Nevyžádaný telemarketing je v řadě případů v rozporu se zákonem. Jak se bránit?',
        'body': (
            'Nevyžádané telefonáty s nabídkou produktů či služeb obtěžují čím dál více lidí. '
            'Mnohdy přitom jde o jednání, které je v rozporu se zákonem o některých službách '
            'informační společnosti i s pravidly ochrany osobních údajů.\n\n'
            'Poradíme, jak takové volání odmítnout, jak si stěžovat u dozorových úřadů a kdy '
            'má smysl se bránit i právní cestou.'
        ),
    },
]


def add_posts(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    for post in POSTS:
        BlogPost.objects.get_or_create(slug=post['slug'], defaults=post)


def remove_posts(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    BlogPost.objects.filter(slug__in=[p['slug'] for p in POSTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_posts, remove_posts),
    ]
