"""Anglické překlady pro klíče použité v core.templatetags.edit_tags (tagy {% t %}, {% edit %}, {% editblock %}).

Klíč = stejný `key`, jaký se používá v šabloně. Pro {% t %} (UI popisky, které nejsou
editovatelné adminem) i pro výchozí text {% edit %}/{% editblock %} (dokud ho admin nepřepíše).
"""

EN = {
    # --- Navigace / header ---
    'nav_home': 'Home',
    'nav_about': 'About us',
    'nav_cooperation': 'How we work together',
    'nav_fees': 'Fees',
    'nav_references': 'References',
    'nav_blog': 'Blog',
    'nav_contact': 'Contact',
    'header_cta_contact': 'Contact us',
    'nav_toggle_label': 'Open menu',

    # --- Footer ---
    'footer_heading_contact': 'Contact',
    'footer_heading_find_us': 'Find us',
    'footer_heading_databox': 'Data box',
    'footer_label_email': 'E-mail',
    'footer_label_phone': 'Phone',
    'footer_nav_home': 'Home',
    'footer_nav_booking': 'Booking',
    'footer_nav_reviews': 'Reviews',
    'footer_nav_faq': 'FAQ',
    'footer_nav_privacy': 'Privacy',
    'newsletter_heading': 'Newsletter',
    'newsletter_text': 'New articles and news straight to your inbox.',
    'newsletter_placeholder': 'Your e-mail',
    'newsletter_button': 'Subscribe',

    # --- Editable content defaults (home) ---
    'home_hero_title': 'Lajsek Legal<br>Law &amp; mediation',
    'home_hero_subtitle': 'Modern office, modern methods',
    'home_hero_button': 'Contact the office',
    'home_services_title': 'Areas of legal practice',
    'home_about_title': 'About us',
    'home_about_text': 'Vladimír Lajsek is an attorney and mediator in Prague, specialising in litigation and mediation, real estate law, intellectual property, GDPR, and contract law.',
    'home_about_link': 'More about the office',
    'home_references_title': 'References',
    'home_references_disclaimer': 'Under the attorney code of ethics, attorneys are prohibited from disclosing any information about their clients. We fully respect this rule.<br><br>Below, however, are a few words about our services:',
    'home_references_link': 'View references',
    'home_blog_title': 'Blog',
    'home_blog_link': 'All articles',
    'home_cta_title': 'Need legal help?',
    'home_cta_button': 'Contact',
    'home_reviews_link': 'Read client reviews',
    'home_booking_title': 'Book a meeting online',
    'home_booking_text': 'Pick an available time from the calendar and set up a consultation in a couple of clicks.',
    'home_booking_link': 'Go to booking',
    'home_faq_title': 'Frequently asked questions',
    'home_faq_text': 'Answers to the most common questions about working with us, pricing, and our legal services.',
    'home_faq_link': 'View FAQ',
    'home_blog_post1': 'Chat Control: protecting children, or the start of a new era of digital surveillance?',
    'home_blog_post2': 'What counts as normal wear and tear? A practical, plain-language guide',
    'home_blog_post3': 'Annoying sales calls: what to do when a company calls you uninvited',

    # --- About page ---
    'about_title': 'About us',

    # --- Cooperation page ---
    'cooperation_title': 'How we work together',
    'cooperation_lead': 'Modern, efficient, and to your full satisfaction!',

    # --- Fees page ---
    'fees_title': 'Fees',

    # --- References page ---
    'references_title': 'References',
    'references_disclaimer': 'Under the attorney code of ethics, attorneys are prohibited from disclosing any information about their clients. We fully respect this rule – below, however, are a few words about our services.',
    'references_client_reviews_title': 'Reviews from clients',
    'references_write_title': 'Write us a reference',
    'references_moderation_note': 'Your reference will be published after approval.',
    'references_submit': 'Submit reference',

    # --- Contact page ---
    'contact_title': 'Contact',
    'contact_lead': 'Reach us by e-mail, by phone, or write a few lines using the form below – we will get back to you by the next business day at the latest.',
    'contact_card_title': 'Lajsek Legal',
    'contact_card_text': 'The law office of Vladimír Lajsek is located in the centre of Prague 3, just a few minutes from the Jiřího z Poděbrad metro station. Consultations take place in person at the office, by phone, or online.',
    'contact_form_title': 'Write to us',
    'contact_form_text': 'Briefly describe your case – we will get back to you by the next business day at the latest.',
    'contact_submit': 'Send message',

    # --- Privacy page ---
    'privacy_title': 'Privacy policy',

    # --- Service pages: shared "Nezávazně konzultovat" CTA ---
    'service_cta': 'Get a no-obligation consultation',
    'service_features_title': 'What we take care of for you',

    'spory_a_mediace_title': 'Litigation and mediation',
    'spory_a_mediace_lead': (
        'Representation in civil and commercial disputes, from preparing the claim to court hearings '
        '– and, where it makes sense, resolving the dispute out of court.'
    ),
    'nemovitosti_title': 'Real estate',
    'nemovitosti_lead': 'Legal services for buying, selling, and leasing real estate – from the contract to the land registry entry.',
    'smlouvy_title': 'Contracts',
    'smlouvy_lead': 'Drafting and reviewing contracts so they are clear, enforceable, and protect your interests.',
    'dusevni_vlastnictvi_title': 'Intellectual property',
    'dusevni_vlastnictvi_lead': 'Protection of copyright, trademarks, and know-how in both the physical and digital environment.',
    'gdpr_title': 'Personal data and GDPR',
    'gdpr_lead': 'Setting up personal data processing in line with GDPR – clearly and without unnecessary bureaucracy.',
    'mediace_title': 'Mediation',
    'mediace_lead': 'Accredited mediation as a faster and less confrontational route to an agreement than going to court.',

    # --- Blog ---
    'blog_title': 'Blog',
    'blog_lead': 'Short articles and notes from the world of law that can be useful in everyday life and business.',
    'blog_read_more': 'Read the full article',
    'blog_empty': 'There are no articles here yet.',
    'blog_back': 'Back to blog',
    'blog_edit_in_dashboard': 'Edit in dashboard',

    # --- Booking ---
    'booking_title': 'Book a meeting',
    'booking_lead': 'Choose an available time slot and fill in a short form – we will send you a confirmation by e-mail.',
    'booking_step1': '1. Choose a time',
    'booking_step2': '2. Your details',
    'booking_no_slots': 'There are no available time slots at the moment, please contact us directly.',
    'booking_submit': 'Book the meeting',
    'booking_selected_prefix': 'Selected time:',
    'booking_select_alert': 'Please choose a meeting time.',
    'booking_pick_day': 'First, choose a day',
    'booking_no_slots_day': 'No available time on this day.',

    # --- Reviews ---
    'reviews_title': 'Reviews',
    'reviews_write_title': 'Write a review',
    'reviews_moderation_note': 'Your review will be published after approval.',
    'reviews_submit': 'Submit review',
    'reviews_empty': 'There are no reviews here yet.',

    # --- FAQ ---
    'faq_title': 'FAQ',
    'faq_lead': 'Answers to the most common questions about working with us and our legal services.',
    'faq_search_placeholder': 'Search questions…',
    'faq_empty': 'There are no questions here yet.',
    'faq_no_match': 'No question matches your search.',
    'faq_cta_text': "Didn't find an answer to your question?",
    'faq_cta_button': 'Write to us',

    # --- Shared form field labels ---
    'form_label_name': 'Name',
    'form_label_email': 'E-mail',
    'form_label_phone': 'Phone',
    'form_label_subject': 'Subject',
    'form_label_message': 'Message',
    'form_label_description': 'Description',
    'form_label_rating': 'Rating',
    'form_label_review_text': 'Review',

    # --- Contact page: info list + form ---
    'contact_info_address': 'Address',
    'contact_info_hours': 'Opening hours',
    'contact_info_hours_value': 'Monday–Friday 9am–6pm',
    'contact_info_databox': 'Data box',

    # --- Language switcher ---
    'lang_switch_label': 'Language',

    # --- 404 ---
    'error_404_title': 'Page not found',
    'error_404_text': "The page you're looking for doesn't exist or has moved. Try one of the links below.",

    # --- SEO meta tags: title (<title>/og:title/twitter:title) + description ---
    'meta_title_home': 'Attorney & Mediator in Prague | Lajsek Legal',
    'meta_desc_home': 'Law office of Vladimír Lajsek in Prague – litigation, mediation, real estate, contracts, GDPR. Book a free consultation today.',

    'meta_title_about': 'About Attorney Vladimír Lajsek | Lajsek Legal Prague',
    'meta_desc_about': 'Vladimír Lajsek, attorney and mediator in Prague with extensive experience in the judiciary and top law firms. Learn about his background.',

    'meta_title_cooperation': 'How We Work Together | Lajsek Legal Prague',
    'meta_desc_cooperation': 'See how easy and fast it is to work with Lajsek Legal in Prague – from first contact to resolving your case.',

    'meta_title_fees': 'Attorney Fees & Pricing | Lajsek Legal Prague',
    'meta_desc_fees': 'Clear information about legal service fees at Lajsek Legal in Prague. Find out how much a consultation or representation costs.',

    'meta_title_references': 'Client References & Reviews | Lajsek Legal Prague',
    'meta_desc_references': 'Read references and experiences from clients of Lajsek Legal in Prague. Share your own review after working with us.',

    'meta_title_contact': 'Contact | Lajsek Legal Attorney Prague',
    'meta_desc_contact': 'Contact Lajsek Legal in Prague – phone, e-mail, address, and contact form. We reply by the next business day at the latest.',

    'meta_title_privacy': 'Privacy Policy | Lajsek Legal',
    'meta_desc_privacy': 'Information on how Lajsek Legal processes personal data of website visitors and clients.',

    'meta_title_spory_a_mediace': 'Litigation & Mediation in Prague | Lajsek Legal',
    'meta_desc_spory_a_mediace': 'Representation in civil and commercial disputes plus out-of-court mediation. Attorney Vladimír Lajsek helps you find the best solution.',

    'meta_title_nemovitosti': 'Real Estate Law Prague | Lajsek Legal',
    'meta_desc_nemovitosti': 'Full legal service for buying, selling, and leasing real estate in Prague – contracts, land registry, easements. Free consultation.',

    'meta_title_smlouvy': 'Contract Drafting & Review Prague | Lajsek Legal',
    'meta_desc_smlouvy': 'Drafting, reviewing, and enforcing business and civil contracts by a Prague law office. Protect your interests with a contract expert.',

    'meta_title_dusevni_vlastnictvi': 'Intellectual Property Law Prague | Lajsek Legal',
    'meta_desc_dusevni_vlastnictvi': 'Protection of trademarks, copyright, and know-how in Prague. An IP attorney to help defend your ideas and brand.',

    'meta_title_gdpr': 'GDPR Compliance for Businesses Prague | Lajsek Legal',
    'meta_desc_gdpr': 'GDPR-compliant personal data processing setup for businesses and e-shops in Prague. Policies, processor agreements, incident handling.',

    'meta_title_mediace': 'Mediation Services Prague | Lajsek Legal',
    'meta_desc_mediace': 'Accredited mediation in Prague – a faster, cheaper way to reach agreement than going to court. Resolve disputes amicably.',

    'meta_title_blog': 'Legal Blog | Lajsek Legal Prague',
    'meta_desc_blog': 'Practical legal advice, law updates, and tips from attorney Vladimír Lajsek. Read about contracts, GDPR, disputes, and real estate.',

    'meta_title_booking': 'Book a Consultation Online | Lajsek Legal Prague',
    'meta_desc_booking': 'Book an online consultation with attorney Vladimír Lajsek in Prague. Pick a free slot from the calendar and schedule in a few clicks.',

    'meta_title_faq': 'FAQ – Legal Services Prague | Lajsek Legal',
    'meta_desc_faq': 'Answers to the most common questions about working with us, pricing, and legal services at Lajsek Legal in Prague.',

    # --- Shared footer content blocks (editblock defaults) ---
    'footer_contact_text': 'The most effective way to reach us is by e-mail, or you can give us a call.',
    'footer_address': '2 Chrudimská 1418, 130 00 Prague 3',
    'footer_hours': 'Monday – Friday: 9am–6pm',
    'footer_databox': '5yzxazh',
    'footer_tagline': 'Modern office, modern methods',

    # --- Cooperation steps ---
    'cooperation_steps': '''
        <div class="steps">
          <div class="step"><span>1</span><div><p>
            Feel free to contact me. Preferably by e-mail at
            <strong>vlajsek@lajseklegal.cz</strong>. Describe your problem in the e-mail.
            You can attach scans of relevant documents right away.
          </p></div></div>
          <div class="step"><span>2</span><div><p>
            I will reply <strong>within 2 days</strong> at the latest (and follow up with
            questions if needed). We can also meet, either in person or online – whichever
            you prefer.
          </p></div></div>
          <div class="step"><span>3</span><div><p>
            I will study your problem in detail, propose the most effective solution, and
            prepare a price estimate. I will send everything to you
            <strong>for review beforehand</strong>.
          </p></div></div>
          <div class="step"><span>4</span><div><p>
            If you agree, I will send the documentation for our cooperation (contract, power
            of attorney, etc.). For your convenience, it is enough to send back
            <strong>a signed scan by e-mail</strong>.
          </p></div></div>
          <div class="step"><span>5</span><div><p>
            I will start actively working on your problem. All to your
            <strong>maximum satisfaction</strong>.
          </p></div></div>
        </div>
    ''',

    'fees_content': '''
        <h2>Legal services agreement</h2>
        <div class="fee-list">
          <div><strong>Hourly rate</strong>Most commonly an hourly rate of approx. CZK 3,000/hour (varies by complexity)</div>
          <div><strong>Invoicing</strong>Invoiced monthly, billed in 15-minute increments</div>
          <div><strong>Out-of-pocket expenses</strong>A separate flat fee for out-of-pocket expenses (phone, printing, office supplies)</div>
          <div><strong>Other costs</strong>Travel, translations, court fees – billed separately</div>
          <div><strong>Statutory tariff</strong>Where no price is agreed, the statutory attorney tariff applies (Decree No. 177/1996 Coll.)</div>
        </div>
    ''',

    'references_quotes': '''
        <div class="quotes">
          <blockquote>
            <p>As the managing director of a company, I had the good fortune to work with
            attorney Vladimír Lajsek on our development projects. His legal advice was
            crucial at many stages – from project financing to preparing and reviewing
            transfer documentation. Mr. Lajsek stands out not only for his professional
            expertise and deep knowledge of real estate law, but also for his ability to
            find practical and effective solutions to complex situations. I confidently
            recommend him to anyone looking for not just an excellent lawyer, but also a
            reliable partner for their development business.</p>
            <footer><span class="avatar">P</span><span class="who"><strong>Pavel</strong><span>Entrepreneur and developer</span></span></footer>
          </blockquote>
          <blockquote>
            <p>Over many years, in both my professional and personal life, I have used the
            services of several law firms. For several years now I have preferred Lajsek
            Legal. I greatly appreciate the precision and care that Dr. Lajsek devotes to
            legal matters. He responds to my needs very quickly, looks for the best possible
            solutions, and explains things clearly and understandably. I can warmly
            recommend Dr. Lajsek.</p>
            <footer><span class="avatar">E</span><span class="who"><strong>Eva</strong><span>In-house lawyer</span></span></footer>
          </blockquote>
          <blockquote>
            <p>Dr. Lajsek saved us a great deal of money, and probably the entire company,
            when he won a critical business dispute for us. Our case looked almost hopeless
            at the start, but Dr. Lajsek prepared our defence so perfectly that we ultimately
            won the dispute. Many thanks!</p>
            <footer><span class="avatar">M</span><span class="who"><strong>Martin</strong><span>Founder and CEO of a technology company</span></span></footer>
          </blockquote>
          <blockquote>
            <p>I am grateful to Mr. Lajsek for his quick response and evident care for my
            interests from the very beginning. That gave me confidence at a time when I
            needed it most.</p>
            <footer><span class="avatar">K</span><span class="who"><strong>Kryštof</strong><span>Entrepreneur and startup founder</span></span></footer>
          </blockquote>
        </div>
    ''',

    'privacy_content': '''
        <h2>Personal data protection</h2>
        <p>The data controller is Vladimír Lajsek, attorney, with registered office at
        2 Chrudimská 1418, 130 00 Prague 3. Contact:
        <a href="mailto:vlajsek@lajseklegal.cz">vlajsek@lajseklegal.cz</a>.</p>
        <h3>What data we process and why</h3>
        <ul>
          <li>contact details and the content of your enquiry, so that we can respond and assess the possibility of cooperation,</li>
          <li>data necessary for performing the legal services agreement and the attorney's statutory obligations,</li>
          <li>technical data necessary for the safe operation of the website.</li>
        </ul>
        <p>We process data for as long as necessary for the given purpose, or as required by
        law. You have the right to access, rectify, erase, restrict processing, object, and
        lodge a complaint with the Office for Personal Data Protection.</p>
        <div class="disclaimer"><strong>Attorney confidentiality:</strong> Information obtained
        while providing legal services is protected by the statutory duty of confidentiality.</div>
    ''',

    'about_bio_content': '''
        <p>Vladimír Lajsek is an attorney and mediator in Prague. He specialises mainly in
        litigation and mediation, real estate law, intellectual property law, personal data
        protection and GDPR, and contract law.</p>
        <h2>Experience</h2>
        <p>He previously worked in the judiciary (successively in the civil, criminal, and
        enforcement divisions, and as court spokesperson) and as in-house counsel at a
        leading bank. He then gained experience at major law firms, including the largest
        and most renowned Czech firm, HAVEL &amp; PARTNERS. This naturally led to founding
        his own practice, Lajsek Legal. In 2024 he expanded his practice to include
        mediation, having obtained a certificate from an accredited training programme.</p>
        <h2>Education</h2>
        <p>He is a graduate of the Faculty of Law at Charles University (Mgr., JUDr., and
        Ph.D. degrees), where he briefly served on the Academic Senate and later also
        taught. He went on to complete postgraduate MBA studies at the University of
        Economics in Prague, in Real Estate and Valuation at the Faculty of Finance and
        Accounting, and the Innovation Project Management programme at the Czech Technical
        University (Ing.).</p>
        <p>In the past he completed study stays at Lancaster University in the United
        Kingdom and at the Technische Universität Dresden in Germany. He also attended
        specialised studies at the Institute of Industrial Property Education at the
        Industrial Property Office.</p>
        <h2>Awards and activities</h2>
        <p>In 2010 he won the SVOČ competition, and in 2019 placed 3rd in the IUS et
        SOCIETAS competition. Between 2010 and 2012 he served as deputy chair of the
        Všehrd Association of Czech Lawyers and editor-in-chief of the Všehrd legal
        journal, where he remains a member of the editorial board to this day. Since 2020
        he has been a member of the Conciliation Board of the Všehrd Association. He has
        also completed a number of internships, notably at the Senate of the Czech Republic
        and the Parliamentary Institute, and served as an external legislative adviser to
        the Constitutional Law Committee of the Chamber of Deputies. In 2021 he was elected
        by the Assembly of the Czech Bar Association to the Disciplinary Committee, and in
        2025 to the Audit Committee, where he still serves today.</p>
        <h2>Languages</h2>
        <p>He speaks English, German, French, and Russian. In English he also works as a
        legal translator – in 2024 he obtained a certificate from a supplementary
        programme at the Faculty of Law, Charles University.</p>
        <h2>Selected publications</h2>
        <p>He is the author of the book <em>Přísedící a laický prvek v justici</em> (Lay
        judges and the lay element in the judiciary) and numerous academic articles,
        mainly in the prestigious journals Právník and Právní rozhledy. Publication titles
        below are kept in their original Czech, as is customary for academic citations.</p>
        <ul class="pub-list">
          <li>LAJSEK, V.: <em>Přísedící a laický prvek v justici.</em> Praha: Leges, 2020, 182 s. ISBN 978-80-7502-459-6.</li>
          <li>LAJSEK, V.: Kritické zamyšlení nad ustanovováním soudců v ČR. <em>Právní rozhledy,</em> 2020, roč. 28, č. 18, str. 627–637. ISSN 1210-6410.</li>
          <li>LAJSEK, V.: Přísedící a zásada zákonného soudce v českém právním řádu. <em>Právník,</em> 2019, roč. 158, č. 11, str. 1031–1045. ISSN 0231-6625.</li>
          <li>LAJSEK, V.: Náležitosti předžalobní výzvy podle § 142a OSŘ. <em>Právní rozhledy,</em> 2016, roč. 24, č. 13–14, str. 489–496. ISSN 1210-6410.</li>
          <li>LAJSEK, V.: Rozdíl mezi kvalifikovanou a jednoduchou výzvou k plnění. <em>Právní rádce,</em> 2016, roč. 24, č. 5, str. 38–40. ISSN 1210-4817.</li>
          <li>LAJSEK, V.: Starší právo k autorskému dílu jako relativní důvod pro odmítnutí zápisu ochranné známky. <em>Právní rozhledy,</em> 2015, roč. 23, č. 7, str. 237–242. ISSN 1210-6410.</li>
          <li>LAJSEK, V.: Vliv Vorwissen, Vorverständnis a hunch theory na rozhodování soudců. <em>Právník,</em> 2012, roč. 151, č. 6, str. 586–604. ISSN 0231-6625.</li>
          <li>LAJSEK, V.: Pojetí teleologické metody interpretace v českém právním prostředí. <em>Právník,</em> 2011, roč. 150, č. 7, str. 633–654. ISSN 0231-6625.</li>
          <li>LAJSEK, V.: Die ehrenamtlichen Richter in der Tschechischen Republik. <em>Deutsch-Polnische Juristen-Zeitschrift,</em> 2020, roč. 12, č. 1–2, str. 42–45. ISSN 1615-9063.</li>
          <li>LAJSEK, V.: The Patentability of Software in the Countries of the European Union. In: Šmejkal, V. et al.: <em>Current EU Law in the Field of Information Technology.</em> Berlin: RWW, 2016, str. 9–26. ISBN 978-3-946915-02-7.</li>
          <li>LAJSEK, V.: K čemu je územní plán a co v něm prověřovat. Epravo.cz, 22. 4. 2022.</li>
          <li>LAJSEK, V.: Vady nemovitých věcí. Epravo.cz, 23. 2. 2022.</li>
          <li>LAJSEK, V.: Změny v oblasti telemarketingu. Epravo.cz, 13. 1. 2022.</li>
          <li>LAJSEK, V.: Cookies – jak budou nově fungovat? Epravo.cz, 22. 12. 2021.</li>
          <li>LAJSEK, V.: Zakládání nízkonákladových s. r. o. Epravo.cz, 9. 6. 2021.</li>
          <li>LAJSEK, V.: Novinky ve smlouvách o výkonu funkce. Epravo.cz, 29. 1. 2021.</li>
          <li>LAJSEK, V.: Novinky v odpovědnosti statutárních orgánů. Epravo.cz, 20. 1. 2021.</li>
          <li>LAJSEK, V.: Jak justice přichází o asistenty. Jiné právo, 11. 8. 2019.</li>
          <li>LAJSEK, V.: Kmenové buňky, patenty a ESD – „One size fits all?“. Jiné právo, 16. 5. 2014.</li>
          <li>LAJSEK, V.: Právo na nerušený výkon veřejné funkce. Všehrd – Spolek českých právníků.</li>
        </ul>
    ''',

    'spory_a_mediace_features': '''
        <h2>What we take care of for you</h2>
        <div class="fee-list">
          <div><strong>Preparing and filing the claim</strong>Analysis of the claim, gathering evidence, and drafting the claim or the statement of defence.</div>
          <div><strong>Court representation</strong>Attendance at hearings, procedural strategy, and communication with the opposing party and the court.</div>
          <div><strong>Mediation as an alternative</strong>Where there is a realistic chance of agreement, we offer an out-of-court solution through mediation.</div>
          <div><strong>Enforcement and debt recovery</strong>Recovering receivables as well as defending against wrongfully conducted enforcement proceedings.</div>
        </div>
    ''',
    'nemovitosti_features': '''
        <h2>What we take care of for you</h2>
        <div class="fee-list">
          <div><strong>Purchase and gift contracts</strong>Drafting and reviewing contracts, escrow of the purchase price, negotiating with the other party.</div>
          <div><strong>Land registry entry</strong>Preparing the application for entry and communicating with the land registry office.</div>
          <div><strong>Easements and liens</strong>Setting up and reviewing third-party rights to the property.</div>
          <div><strong>Lease relationships</strong>Lease agreements for flats, houses, and commercial premises, resolving disputes with tenants.</div>
        </div>
    ''',
    'smlouvy_features': '''
        <h2>What we take care of for you</h2>
        <div class="fee-list">
          <div><strong>Business contracts</strong>Purchase contracts, work contracts, framework and distribution agreements.</div>
          <div><strong>Terms and conditions</strong>Setting up terms and conditions for e-shops and other businesses.</div>
          <div><strong>Contract review</strong>Reviewing contracts presented by the other party and flagging risky clauses.</div>
          <div><strong>Enforcing contracts</strong>Handling situations where the other party fails to perform the contract.</div>
        </div>
    ''',
    'dusevni_vlastnictvi_features': '''
        <h2>What we take care of for you</h2>
        <div class="fee-list">
          <div><strong>Trademarks</strong>Advice on filing and protecting trademarks.</div>
          <div><strong>Copyright</strong>Licence agreements, protection of copyrighted works, and addressing their unauthorised use.</div>
          <div><strong>IT and software</strong>Software development agreements, licensing, and know-how protection.</div>
          <div><strong>Intellectual property disputes</strong>Representation in cases of unauthorised use of protected rights.</div>
        </div>
    ''',
    'gdpr_features': '''
        <h2>What we take care of for you</h2>
        <div class="fee-list">
          <div><strong>Personal data processing policies</strong>Preparing documentation for websites, e-shops, and internal company processes.</div>
          <div><strong>Data processing agreements</strong>Setting up relationships with processors and suppliers.</div>
          <div><strong>Security incidents</strong>Handling data breaches and communication with the Office for Personal Data Protection.</div>
          <div><strong>Internal GDPR audit</strong>Checking whether the company processes personal data in line with the rules.</div>
        </div>
    ''',
    'mediace_features': '''
        <h2>What we take care of for you</h2>
        <div class="fee-list">
          <div><strong>Business disputes</strong>Mediation between business partners aimed at preserving the working relationship.</div>
          <div><strong>Neighbour and property disputes</strong>Resolving disputes over real estate, land boundaries, or joint property.</div>
          <div><strong>Family matters</strong>Mediation of broader family and property-related questions.</div>
          <div><strong>Out-of-court settlement</strong>Drafting an agreement that is binding on both parties and replaces a court decision.</div>
        </div>
    ''',
}
