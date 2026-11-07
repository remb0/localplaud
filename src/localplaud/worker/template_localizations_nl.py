"""Nederlandse vertalingen van de ingebouwde Plaud-sjablonen."""

DUTCH = {
    "plaud-autopilot": {
        "name": "Slimme samenvatting (automatisch)",
        "description": "Kies een passende samenvattingsstructuur voor de inhoud van de opname.",
        "instructions": """Kies de samenvattingsstructuur die het beste bij de inhoud past. Pas de
indeling aan het soort opname aan, bijvoorbeeld een vergadering, interview of
lezing. Gebruik bij een specialistische behoefte, zoals medische SOAP-notities,
bij voorkeur het daarvoor bedoelde specialistische sjabloon.
Schrijf in het Nederlands. Behoud belangrijke details en onzekerheden.
Voeg geen feiten, besluiten of actiepunten toe die niet uit de opname blijken.""",
    },
    "plaud-key-metrics": {
        "name": "Belangrijke cijfers en gegevens",
        "description": "Verzamel getallen, eenheden en bijbehorende context in een overzichtelijke tabel.",
        "instructions": """Werk als een professionele data-analist. Zoek alle numerieke gegevens in
het transcript, bepaal hun betekenis en orden ze overzichtelijk.

Extractieregels:
- Waarde: neem het getal zelf over. Herleid indirecte verwijzingen, zoals 'dat
  aantal', tot een eerder genoemde concrete waarde als de bron dit ondersteunt.
- Kengetal: bepaal uit de omliggende beschrijvingen de formele naam van het
  gegeven. Kies de meest gebruikte beschrijving; geef bij gelijke frequentie
  voorrang aan de eerstgenoemde beschrijving.
- Eenheid: gebruik de context voor een onderbouwde eenheid, zoals dagen,
  procenten, een valuta of stuks. Noteer 'niet genoemd' als de eenheid ontbreekt.
- Context: beschrijf bondig de relevante achtergrond, aannames, besluiten en
  discussiepunten rond iedere waarde.

Schrijf in het Nederlands. Gebruik een Markdown-tabel met de kolommen Waarde,
Kengetal, Eenheid en Context. Houd niet-gerelateerde getallen gescheiden en
verzin geen ontbrekende waarden of eenheden.""",
    },
    "plaud-intent-analysis": {
        "name": "Analyse van gespreksintenties",
        "description": "Onderzoek mogelijke bedoelingen met concrete onderbouwing en expliciete onzekerheid.",
        "instructions": """Werk als een ervaren, neutrale communicatieanalist. Onderzoek welk
achterliggend doel de spreker mogelijk wil bereiken. Houd de analyse praktisch
en objectief. Benoem afgeleide bedoelingen altijd als hypothesen.

Gebruik vier invalshoeken:
1. Emotioneel verloop: zoek momenten met de sterkste aantoonbare emotionele lading.
2. Betekenisvolle stilte: betrek pauzes of aarzeling uitsluitend als deze
   daadwerkelijk in de bron zijn vastgelegd.
3. Woordkeuze: beschouw overmatig uitleggen of bagatelliseren als mogelijke,
   niet als zekere, aanwijzingen voor onzekerheid of vermijding.
4. Context: houd rekening met culturele conventies, formaliteit en beleefdheid.

Schrijf een beknopte Nederlandstalige analyse met deze onderdelen:
- Waarschijnlijkste intentie: één centrale hypothese met hoge, gemiddelde of lage
  zekerheid.
- Onderbouwing: specifiek waarneembaar gedrag en nauwkeurig overgenomen citaten.
- Aanbevolen gespreksaanpak: een op de bron gebaseerde aanpak, duidelijk
  onderscheiden van wat daadwerkelijk is gezegd.
Verzin geen non-verbale signalen of verborgen motieven.""",
    },
    "plaud-meeting-narrative": {
        "name": "Uitgebreid verhalend vergaderverslag",
        "description": "Beschrijf het gesprek, de bijdragen, besluiten en vervolgstappen in chronologische volgorde.",
        "instructions": """Zet het vergadertranscript om in een volledig, gedetailleerd en
chronologisch verhaal. Behoud de belangrijkste onderwerpen, discussies,
besluiten, actiepunten, bijdragen van deelnemers en het verloop van het gesprek.
Beschrijf wie onderwerpen inbracht, welke argumenten en gegevens werden genoemd,
hoe anderen reageerden en welke besluiten, afwegingen, afwijkende meningen en
openstaande vragen daaruit voortkwamen.

Neem alle expliciet afgesproken acties, verantwoordelijken en deadlines op.
Behoud de toon en sfeer voor zover deze uit het transcript blijken. Sluit af met
de genoemde vervolgstappen, vervolgafspraken en afsluitende opmerkingen.
Markeer ontbrekende informatie als 'niet genoemd'; vul niets zelf in.

Schrijf in helder, professioneel Nederlands voor zakelijke lezers, inclusief
belanghebbenden die niet aanwezig waren. Gebruik alinea's en getrouwe citaten,
tussenkoppen bij onderwerpwisselingen en vetgedrukte besluiten en actiepunten.
Gebruik geen opsommingen: het resultaat moet als een samenhangend verhaal lezen.
Voeg geen nieuwe feiten, afspraken of citaten toe.""",
    },
    "plaud-lecture-deep-dive": {
        "name": "Verdiepend verslag van een lezing",
        "description": "Leg begrippen, argumenten, voorbeelden, citaten en praktische inzichten uit een lezing vast.",
        "instructions": """Maak een brongetrouw Nederlandstalig verslag van de lezing of presentatie.
Behoud de toon, begrippen en praktische inzichten van de spreker.

Begin met het hoofdthema, de genoemde presentatietitel, belangrijke termen,
metaforen en terugkerende formuleringen. Vat de kernboodschap samen in één of
twee krachtige alinea's. Leg uit waarom die relevant is, welk probleem deze
adresseert of welk blijvend of bijzonder inzicht deze biedt.

Volg de opbouw van de spreker. Verdeel het verslag in benoemde onderdelen of
hoofdstukken. Beschrijf per onderdeel de kerngedachte, het doel en het belang.
Licht de belangrijkste argumenten, begrippen en theorieën toe. Leg genoemde
kaders, modellen, stappen, methoden en hulpmiddelen gedetailleerd uit. Neem de
gebruikte voorbeelden, analogieën, metaforen en korte verhalen op. Benoem
vastgelegde momenten van publieksbetrokkenheid, zoals retorische vragen, grappen,
verrassende cijfers of emotionele verhalen.

Verzamel waar de bron dit toelaat 8 tot 15 getrouwe, duidelijk toegeschreven
citaten: kernachtige uitspraken, inspirerende zinnen, metaforen, definities,
uitdagingen en deelbare inzichten. Kies citaten die zelfstandig begrijpelijk
zijn en binnen het verslag extra betekenis krijgen. Verzin geen citaten om
een minimumaantal te halen. Laat citaten in de oorspronkelijke taal staan;
markeer een eventuele Nederlandse vertaling uitdrukkelijk als vertaling.

Maak een begrippenoverzicht dat als hulpmiddel bij uitleg of onderwijs kan dienen.
Neem waar genoemd theoretische grondslagen, mentale modellen, wetenschappelijke
inzichten, gegevens, onderzoeksresultaten, tegenintuïtieve ideeën en betwiste
aannames op. Geef ieder begrip een korte maar inhoudelijke toelichting.

Formuleer waar de inhoud dit ondersteunt 3 tot 7 praktische, strategische
aanbevelingen voor teams, leidinggevenden of individuen. Schrijf iedere
aanbeveling als richtlijn met een korte onderbouwing uit de lezing. Maak duidelijk
dat dit aanbevelingen zijn, geen door deelnemers afgesproken taken. Benoem
eventueel één eerste stap die de spreker zelf aanbeveelt.

Sluit in toon, stijl, terminologie en ordening aan bij de spreker. Voeg alleen
als de bron er concrete informatie over bevat een onderdeel toe met de titel
'Wat je miste als je er niet bij was', over de presentatie, sfeer, emotionele
omslagpunten, onverwachte momenten of opvallende uitspraken.""",
    },
    "plaud-research-interview": {
        "name": "Onderzoeksinterview",
        "description": "Beschrijf de interviewcontext, belangrijkste bevindingen en een gestructureerd vraag-en-antwoordverslag.",
        "instructions": """Maak een Nederlandstalig interviewverslag. Begin met tijdstip, locatie en
geïnterviewde. Gebruik uitsluitend informatie uit de opname en noteer
'niet genoemd' bij ontbrekende gegevens.

Inleiding: beschrijf de context van het interview en de achtergrond van de
geïnterviewde.
Belangrijkste bevindingen: vermeld de voornaamste inzichten uit het interview.
Interviewverslag: behoud de volgorde van alle vragen en orden de bijbehorende
antwoorden onder iedere vraag. Gebruik meerdere antwoordpunten waar dat helpt.
Voorbeelddata, locaties en namen uit een sjabloon zijn uitsluitend voorbeelden,
nooit feiten over dit interview. Voeg geen ontbrekende antwoorden toe.""",
    },
    "plaud-interview": {
        "name": "Interviewverslag",
        "description": "Orden achtergrond, vragen en antwoorden, belangrijke inzichten en uitspraken die beoordeling vragen.",
        "instructions": """Orden het interview in achtergrond, vragen en antwoorden, en inzichten.
Schrijf het verslag in het Nederlands.

Achtergrond: benoem de geïnterviewde en het onderwerp. Markeer kernpunten met ★.
Vragen en antwoorden: vermeld iedere vraag, een samenvatting van het antwoord,
getrouwe directe citaten en uitsluitend een aantoonbare emotionele toon.
Vermeld antwoordduur alleen als tijdstempels dit ondersteunen. Behoud genoemde
gegevens, zoals jaarproductie, en markeer aantoonbaar vermeden onderwerpen met ◆.
Inzichten: benoem inzichten over de sector en markeer controversiële uitspraken
met ◆ voor menselijke beoordeling. Deze markering is geen juridisch oordeel.
Voeg gedrag tussen haken, zoals [lacht] of [pauze], uitsluitend toe wanneer dit
in de bron staat. Verzin geen citaten, tijdsduren, emoties of non-verbaal gedrag.
Behoud de oorspronkelijke taal van directe citaten; markeer vertalingen als zodanig.""",
    },
    "plaud-full-transcript": {
        "name": "Volledig transcript voor extern gebruik",
        "description": "Een volledig chronologisch transcript, zonder samenvatting of interpretatie.",
        "instructions": """Geef alles uit het aangeleverde transcript getrouw en volledig weer,
zonder de inhoud samen te vatten, te interpreteren of te veranderen.
Behoud exact de chronologische volgorde en benoem sprekerwisselingen als de bron
daarvoor voldoende informatie bevat, bijvoorbeeld 'Arts' en 'Patiënt'.
Voeg geen commentaar, titels, uitleg, samenvattingen of conclusies toe.
Lever een volledig tekstueel transcript voor externe analyse of archivering.
Gebruik duidelijke opmaak en regeleinden tussen bijdragen. Behoud de
oorspronkelijke gesproken taal: vertaal het transcript niet en verzin geen
woorden die in de bron ontbreken.""",
    },
    "plaud-meeting-minutes": {
        "name": "Uitgebreide vergadernotulen",
        "description": "Begin met besluiten en actiepunten en geef daarna gedetailleerde chronologische notulen.",
        "instructions": """Maak professionele Nederlandstalige vergadernotulen in twee stappen:
behoud eerst alle inhoudelijke informatie en orden die vervolgens voor de lezer.
Reconstrueer het gesprek zorgvuldig; vereenvoudig het niet ten koste van details.
Werk als een nauwkeurige redacteur en voeg geen speculatieve analyses toe.

Brongetrouwheid staat voorop. Verwijder stopwoorden en maak van spreektaal
heldere professionele formuleringen, zonder betekenis of inhoudelijke details
te veranderen. Markeer bij verwerking in delen onvolledige begin- of eindzinnen,
zodat die later met de omliggende context kunnen worden samengevoegd.

Bedien zowel lezers die een overzicht nodig hebben als lezers die details zoeken.
Begin met twee samengevoegde lijsten: expliciet afgesproken actiepunten en
belangrijke besluiten. Behoud verantwoordelijken, deadlines, voorwaarden en
onzekerheden. Maak van een open vraag of suggestie geen besloten actiepunt.
Geef daarna gedetailleerde chronologische notulen. Gebruik per onderwerpblok
een bruikbaar tijdstip als dit bekend is, een vetgedrukte kernzin en ingesprongen
opsommingen die de inhoudelijke details van de discussie behouden.
Noteer 'niet genoemd' bij ontbrekende gegevens en verzin geen afspraken.""",
    },
    "plaud-meeting-highlights": {
        "name": "Belangrijkste inzichten uit een vergadering",
        "description": "Breng blijvend waardevolle inzichten samen in een beknopt, hiërarchisch overzicht.",
        "instructions": """Haal de betekenisvolste en blijvend bruikbare inzichten uit het gesprek,
in plaats van alle details na te vertellen. Kies kwaliteit boven kwantiteit en
concentreer je op ideeën die ook over een jaar nog waarde kunnen hebben.

Geef voorrang aan breed toepasbare observaties boven zeer specifieke meningen,
tegenintuïtieve bevindingen boven vanzelfsprekende bevestigingen, mentale
modellen boven losse conclusies en overdraagbare lessen boven unieke ervaringen.
Maak duidelijk onderscheid tussen eigen gevolgtrekkingen en feiten die
daadwerkelijk in het gesprek zijn genoemd.

Orden de inzichten in een hiërarchisch overzicht met meerdere niveaus.
Elk overkoepelend punt is één bondige zin van maximaal twintig woorden en dekt
de onderliggende punten nauwkeurig. Werk van brede thema's naar specifiekere
inzichten; zet de inhoudelijke observaties op het diepste niveau.
Schrijf in het Nederlands. Houd de structuur logisch en beknopt.""",
    },
}
