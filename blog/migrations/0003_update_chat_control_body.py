from django.db import migrations

SLUG = 'chat-control-ochrana-deti-nebo-digitalni-kontrola'

NEW_BODY = (
    'Evropská unie už delší dobu hledá cestu, jak účinněji bránit sexuálnímu '
    'zneužívání dětí na internetu. Cíl je nesporně správný. Jen málokteré téma '
    'vyvolává tak silnou společenskou shodu. Právě proto je ale nutné zachovat '
    'chladnou hlavu. Návrh známý jako Chat Control totiž neotevírá jen otázku '
    'bezpečnosti dětí, ale také otázku, kam až může stát nebo Unie zajít při '
    'kontrole soukromé komunikace.\n\n'
    'Podstata problému je poměrně jednoduchá. Pokud mají poskytovatelé '
    'komunikačních služeb aktivně vyhledávat podezřelý obsah nebo podezřelé '
    'komunikační vzorce, nevyhnutelně se tím oslabuje důvěrnost soukromých '
    'zpráv. A to je v evropském právu velmi citlivá věc. Soukromá komunikace '
    'není luxus ani technický detail. Je to základní předpoklad svobodného '
    'života. Lidé musí mít možnost psát si s partnerem, dítětem, lékařem, '
    'advokátem nebo přáteli bez pocitu, že jejich zprávy může někdo průběžně '
    'analyzovat.\n\n'
    'Právě zde se střetávají dva silné principy. Na jedné straně stojí '
    'ochrana dětí před závažnou kriminalitou. Na druhé straně právo na '
    'soukromí a důvěrnost komunikace. Často se přitom vytváří dojem, že kdo '
    'kritizuje Chat Control, ten zlehčuje ochranu dětí. To je falešné '
    'dilema. Kritika takové regulace neznamená odmítání ochrany dětí. '
    'Znamená jen to, že i dobře míněná regulace musí mít rozumné meze.\n\n'
    'Z právního hlediska je důležité ještě něco jiného. Evropské soudy už v '
    'minulosti opakovaně řekly, že plošné a nerozlišující zásahy do '
    'elektronické komunikace narážejí na základní práva velmi tvrdě. '
    'Nestačí tedy říct, že cíl je dobrý. Je třeba také prokázat, že zvolený '
    'prostředek je skutečně přiměřený, nezbytný a účinný.\n\n'
    'A právě účinnost je další slabé místo celé debaty. Co když budou '
    'nejvíc sledováni běžní uživatelé, zatímco pachatelé se přesunou do '
    'uzavřených, šifrovaných nebo jinak skrytých komunikačních prostorů? '
    'Co když výsledek bude takový, že slušná většina přijde o část svého '
    'soukromí, ale skutečně nebezpeční lidé si stejně najdou cestu, jak '
    'systém obejít? Pak bychom dostali regulaci, která je současně '
    'invazivní i málo účinná. A to je z pohledu právního státu velmi '
    'špatná kombinace.\n\n'
    'Právě proto se u Chat Control stále častěji mluví o riziku '
    'panoptického efektu. Nejde nutně o to, že by někdo každou zprávu '
    'ručně četl. Stačí už samotné vědomí, že soukromá komunikace může být '
    'automaticky kontrolována. Lidé pak mění své chování. Píší opatrněji. '
    'Vyhýbají se některým tématům. Ztrácejí pocit, že digitální prostor je '
    'skutečně soukromý. To má dopady nejen na intimitu, ale i na svobodu '
    'projevu.\n\n'
    'Debata o Chat Control proto není technickou hádkou o internetových '
    'aplikacích. Je to spor o charakter svobodné společnosti. Ochrana dětí '
    'musí být silná a účinná. Neměla by se ale stát záminkou k tomu, aby '
    'se z výjimečného zásahu stal nový standard běžné komunikace. Jinak '
    'bychom mohli ve jménu bezpečnosti oslabit právě ty svobody, které má '
    'demokratický právní stát chránit.\n\n'
    'Pokud má být podobná regulace přijatelná, musí být úzce cílená, '
    'transparentní a přísně kontrolovaná. Nesmí se proměnit v plošné '
    'sledování všech jen proto, že to technicky jde a politicky se to '
    'dobře obhajuje.'
)


def update_body(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG).update(body=NEW_BODY)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_seed_posts'),
    ]

    operations = [
        migrations.RunPython(update_body, noop),
    ]
