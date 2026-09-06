from django.db import migrations

SLUG = 'co-je-a-co-neni-bezne-opotrebeni'

NEW_BODY = (
    '„To je přece jen běžné opotřebení.“ Věta, která zaznívá hlavně při '
    'vracení bytu, při sporech o kauci nebo při reklamaci starší věci. '
    'Jenže právě tady často vzniká nejvíc nedorozumění. Co je ještě '
    'přirozený následek užívání, a co už je poškození, za které někdo '
    'odpovídá?\n\n'
    'Běžné opotřebení je zjednodušeně řečeno takové zhoršení stavu věci, '
    'které vzniká normálním užíváním a plynutím času. Typicky jde o drobné '
    'známky používání, které se dají očekávat. U bytu to může být '
    'například potřeba nové výmalby po delší době užívání, opotřebené '
    'těsnění nebo jiné běžné stopy každodenního provozu domácnosti.\n\n'
    'Naopak za běžné opotřebení už zpravidla nelze považovat stav, kdy je '
    'věc poškozená tak, že nefunguje, je výrazně znehodnocená nebo její '
    'stav neodpovídá tomu, co lze rozumně očekávat. Rozhodující tedy není '
    'jen to, že je věc „starší“ nebo „používaná“, ale hlavně to, jaký je '
    'konkrétní rozsah poškození a zda jde jen o estetickou stopu, nebo o '
    'skutečný problém.\n\n'
    'Právě u nájmu bytu bývá rozdíl mezi opotřebením a škodou nejčastějším '
    'sporným bodem. Pronajímatel totiž často považuje za škodu i to, co je '
    've skutečnosti jen přirozeným důsledkem běžného užívání. Nájemce '
    'naopak někdy pod běžné opotřebení zahrnuje i to, co už je zjevně nad '
    'jeho rámec. Každý případ je proto potřeba posuzovat jednotlivě – '
    'podle délky užívání, stavu věci při převzetí, způsobu užívání i podle '
    'toho, zda byla dotčena funkčnost.\n\n'
    'Podobné je to i při koupi starší věci, například automobilu nebo '
    'nemovitosti. Samotné stáří věci ještě neznamená, že kupující musí bez '
    'výhrad přijmout jakýkoli technický nebo stavební problém. I starší '
    'věc musí odpovídat tomu, co bylo mezi stranami ujednáno a co lze od '
    'takové věci rozumně očekávat.\n\n'
    'V praxi proto bývá nejdůležitější důkazní stránka věci. Rozhodují '
    'předávací protokoly, fotografie, komunikace mezi stranami, popis vad '
    'i případný odborný posudek. Právě na detailech často záleží, zda '
    'půjde jen o běžné opotřebení, nebo o nárok na náhradu škody či slevu '
    'z ceny.\n\n'
    'Máte spor o kauci, stav vraceného bytu, vady starší nemovitosti nebo '
    'reklamaci použité věci?\n\n'
    'Rychlé a správné právní posouzení může rozhodnout o tom, zda budete '
    'platit, nebo naopak úspěšně vymáhat svůj nárok. V těchto sporech '
    'obvykle nerozhoduje jen „selský rozum“, ale hlavně správné vyhodnocení '
    'konkrétních okolností a důkazů.\n\n'
    'Pokud si nejste jistí, zda jde ve Vašem případě ještě o běžné '
    'opotřebení, nebo už o právně významnou vadu či škodu, je vhodné '
    'situaci posoudit dříve, než vznikne zbytečný spor.'
)


def update_body(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG).update(body=NEW_BODY)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_update_chat_control_body'),
    ]

    operations = [
        migrations.RunPython(update_body, noop),
    ]
