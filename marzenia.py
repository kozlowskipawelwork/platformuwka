'''
chcialbym zrobic platformowke,
z infinite wordem, oraz z fajie by bylo ze z menu

narazie mam
tlo
podloge
bohatera i 2 potworki

chcialbym zrobic
poruszanie sie ze scrollem podlogi, lub tylko tla, w poziomie
a take poruszanie się potworow wzgledem bohatera

jedna koncepcja jest taka ze chcialbym zrobic taka planszke mala w kartezjanie,
i bohater poruszalby sie w takiej iluzji izometrycznosci

lub poprostu platformowka i obiekty poruszalyby sie tylko w poziomie, zobaczymy jak bedzie,

najpierw - dodanie klocuszkow, kolizje z nimi, i zobaczymy jak to bedzie, chyba i tak spoczko
jakbym zrobil jakas baze.

chcialbym tez zrobic jakis maksymalnie cheesy i wredny i trudny gimmick ktory uczynilby
ta gre interesujaca, ale no to zobaczymy.
bede tez pisal na bierząco loga z tego co robie, moze to cos ciekawego da?

30.01.2022 14:01
dodałem do klasy player podstawowy movement, usunalem x i y z kontstruktora,
zeby to w ogole zadziałało, i dodałem input klawiszy.
teraz chciałym zrobic to ze speedami zeby to ladniej plynniej dzialalo,
jak narazie robi taki blit w jedna stronę.

30.01.2022 14:13
zmienic input na pygame key pressed i zaplikowac wersje z techwithtim

30.01.2022 14:34
zadziałało, mam teraz smooth movement u playera. SUPER!
#zaimplementować poruszanie w prawo, i zaraz skok!
stworzylem metode ground and jump, zeby umiescic tam potem key input i mechanike skoku.
moge chyba skonczyc jak narazie, jestem u fluffiego na drugim filmiku 8:41
30.01.2022 15:11
do zrobienia beda także wstepne kolizje,
zrobisz je przydzielajac self_rect.x do self.x itp
30.01.2022
parachute mogloby byc nazwa
chce zeby zltywaly potwory i mozna bylo je zestrzelic. jak narazie chce zrobic zeby potwory
przesuwaly sie wraz z bohaterem.
30.01.2022
dodalem cale poruszanie sie, gra zmienila sie w izometryka, albo topdowna,
i tyle w sumie lece dalej bede zapisywal co zrobilem jak ogarne co zrobilem
ale wychodzi na to ze pygame lepszy od pygame functions dobrze idzie
dobry przekaz leci

31.01.2022
co tu sie stalo...
pora na przejrzenie calego projektu, co mamy
z tego co pamietam, ogarnalem wczoraj kolizje!, trzeba bylo stworzyc pygame.sprite.Sprite init w klasie,
zrobic rect  korzystajac z get_rect i przesuwac go razem z potworkiem przy movemencie.
takze wszystko fajnie!
pora rozkminic scrolling background! niestety ale to jest do feelingu gry bardzo potrzebne.
bardzo cchialbym zobaczyc hp nad potworkami, najlepiej tylko przy kolizji, czy cos
musze pamietac ze za obrazenia przy kolizjach bedzie odpowiadac jakis algorytm, niekoniecznie skomplikowany, ale moze obrazenia broni + sila kontra sila potwora costam to wtedy odejmuje zycie potwora, i chuj.
bron najlepiej bedzie zrobic w osobnej klasie.
chcialbym zrobic takie current weapon, ze wyswietla bron jaka mamy, albo wypisuje, niewazne,
zrobilem 30 pociskow do strzalow, takze strzelanie
#background,
#strzelanie
no i fajnie. przydaloby sie zlapac andrzeja w tym tygodniu, zeby spawnowac wielu na raz, ale dopiero po backgroundzie.
bron moze jest odpowiednio wyjasniona w zeldzie, zobaczymy. mysle ze powinienem ogladac ten tutorial i probowac go zrozumiec jak najmocniej, w ciagu dnia.
najwyrazniej nie ma co sie bac, kolizje rozkminione, bedzie dobrze, dobra robota!
31.01.2022
so, what now?
dalej background reseachuje
yyy
w backgroundzie ogarnalem granice
            if abs(self.x) > 400:
                self.x = 400
                w movie sprawia, ze sie zatrzymuje na granicy
                jak narazie zrobie granice. poprostu


                        if keys[pygame.K_LEFT]:

            #ogarnalem granice
            if self.x > -500:
                self.x = -1000
            self.x += self.speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += -self.speed
            if self.x > 400:
                self.x = 0
        if keys[pygame.K_UP]:
            if abs(self.y) > 100:
                self.y = 100
            self.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:

            if abs(self.y) > 555:
                self.y += 50
            self.y += -self.speed

            to jak wrzucisz w move daje mega poryty efekt

            odleglosci kwadraty teleportuj mnie do dlugosc ekranow i cos

        01.02.2022
        Andrzej zrobil scrolla, musze ogarnac jak to zrobil, zrozumiec system settings, zrobic granice i spawning

        01.02.2022
        zacznijmy od przeczytania calego kodu, moze komentowania
        tak wiec w mainie zostalo wprowadzone system settings, a raczej zmienna ktora uwspolnia x i y playera i background,
        w klasach player i background x i y zamiast 0, 0 jest teraz disp[0] i disp[1] disp jest dodany tez w konstruktorze jako taka wartosc ktora zbieramy
        z zewnatrz.

        poprostu obie te klasy dziela x i y jest on przydzielany z zewnatrz za pomoca tego system settings

        nastepnym razem powinienem dokonac analizy tego jeszcze raz.
        nastepnie przyjzyjmy sie juz creme de la creme, czyli samej klasie backgroundu.
        iluzja poruszania sie po podlodze sklada sie na
        wyblitowaniu 9ciu kopii tla, w takim szczescianie, jakby caly czas poruszamy sie w tym jednym, dzieki granicom,
        ale efekt jest wlasnie taki.
        #przyjdzec sie offsetowi w system settings
        #popatzec i rozpisac sobie(na kartce nawet) gdzie i jak jaki kwadrat bedzie sie znajdywal
        #nastepnie wyrysowac granice
        chce najpierw sprawdzic, czy wszystko bedzie dzialac, jak zmeinie self.x, y z disp na zhardcodowane wartosci self witdth i height.
        no i kurwa jakby dziala tak samo, wiec sobie to tak zmienie, a jak juz bede ogarnaic co to parametryzacja i reformatyzacja kodu, to sb tak zrobie.
        wszystko dziala picus glancus z hardcodowanymi srodkami, player i background, takze jest fajnie, przyjrzec sie potem temu disp
        bo to ulepszenie, ale nie na moja banie oj nienie
        takze zostaje ten background, wyblitowac wszystkie kwadraty pixel perfect, a takze pixel perfect zrobic granice, najlepiej na kartce to zrobie zeby ogarnac
        a tak poza tym to wszystko ladnie i pieknie wyszlo.
        kod do przeczytania jeszcze raz i pelnego zrozumienia, wystudiowac ten rect centering w pygamie, na przyszlosc.
        ale wszystko dziala, wiec jestem bardzo szczesliwy.
        pora zastanowic sie co bedzie po backgroundzie...


        01.02.2022 21:31
        zrobiony background i granice, wszystko dziala, nie wiem czy plynnie bo mam obciazony procek, co juz cos znaczy.
        pora na strzelanie.
        i nagle kolizje sie posypaly.
        i wrocilem je z powrotem, do tego poprawiajac. trzeba od recta odjac 35.
        stworzyc przedmiot, moc go podniesc, rzucic nim i on by sie zatrzymal na potworze
        pocisk rzut colliderec bullet_speed = 0
        jednak hitboxy dalej nie sa takie jakie byc powinne
        ten kod - weapon, tworzy przedmiot na ziemi.
        class Weapon():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen_width = 800
        self.screen_height = 640
        self.x = self.screen_width/2-35
        self.y = self.screen_height/2 -35
        self.speed = 10
        #self.strength = 10 moze odwolanie do player strenght w przyszlosci?
        self.weapon_sprite = pygame.image.load('data/img/weapons/possesed war axe.png').convert_alpha()

        self.rect = self.weapon_sprite.get_rect(center = (self.screen_width/2-35,screen_height-35))
        self.rect.x = self.x
        self.rect.y = self.y
        self.player_mask = pygame.mask.from_surface(self.weapon_sprite)
        self.gravity = 0



    def draw(self):
        screen.blit(self.weapon_sprite, (self.x, self.y))
    def collision(self):
        pass
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += -self.speed
        if keys[pygame.K_UP]:
            self.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.y += -self.speed

    def update(self):
        self.move()
        self.collision()
        self.draw()
        #self.move()

        takze to bedzie mialo szersze o wiele zastosowanie ten kod
        na przyklad zrobic - ze kolizje z danym przedmiootem dodaje hp na przyklad.
        i on znika przy dotknieciu tez
    tak wiec stworzylem szafe oraz topor, postaram sie teraz zaby topor zaczal strzelac
    zrobic ten atak na nested ifach
    trzeba dopracowac pozycje recta bo sie nie zgadza usunac na drugim i zrobic tylko na jednym moglbym sprobowac narysowac go tez zeby go zobaczyc i przesunac

    brakuje lampy czyli hpboosta
    obrazenia lub trafienie.
    przeciwnicy ruszajacy sie, ktorzy by Cie atakowali i ktorzy by strzelali
    juz odemnie to ekwipunek menusy handlarze i bedzie git
    nalozyc recty na kolizje i sprawdzic gdzie sa!
    01:40 02.02.2022
    rect kolizyjny dziwnie sie porusza, nie jest rowny ze sprajtem, trzeba go jakos przesunac
    xd
    dalej nie dziala
    narysowac rect na playerze, zobaczyc jak sie to przesuwa
    definitywnie cos jest nie tak z rectami , musze ogarnac gfdzie co sie przesuwa, narysowac recty w miejscu, upewnic sie ze player rect dziala.

    takze najpierw przesuwanie player recta,
    potem przesuwanie rectow obiektow.
    nie ma stresu. usune wszystkie recty, i zloze je od nowa.
    14:47 02.02.2022
    oczyscic kod z rectow, pousuwac niepotrzebne zmienne
    i potem bedzie sie aplikowac cos
    21:42
    kolizje rozwiazane - od teraz, zamiast obrazkami, blitujemy recty z obrazkami i nimi ruszamy.
    trzeba zaaplikowac w broni.
    jesli mamy juz wstepna koncepcje kolizji oraz broni, to moze teraz podjac sie czegos wiekszego, zaprojektowac feature, na przyklad ekwipunek albo doswiadczenie
    ale fajnie ze sie udalo, przyda mi sie teraz jakas kreatywna energia

    00:00 03/02/2022
    pora wyczyscic kod, bullet.py juz wyczyscilem, kolizje dzialaja, bron tez juz jest rectem, tak samo jak wszystkie juz przedmioty.
    mysle ze pora skupic sie na stworzeniu godnego przeciwnika, ktory bedzie sie ruszal.
    wlasnie wpadla mi koncepcja na autoatak, co jesli bym trzymal klawisz i przy inheritansie i potwora i broni, na granicy jakiejstam
     kazalbym rectowi broni isc w strone potwora? i tak w ta strone bede musial isc, pun intended, bo tak samo bedzie wygladac movement,
     tylko ze bedzie to ruch potwora wobec recta bohatera.
     ######################
     research do health barow,
     koles ogolnie na fstringu to robi, nie mam entuzjazmu zeby to zrobic teraz, ale jest to rozwiazanie do zaaplikowania, jesli cos entuzjastycznie nie przejmie mojej uwagi.
     tak samo z nego health barami, rysuje ladne recty, chyba jest to ostateczne rozwiazanie, tylko ze kwestie ta bede aplikowac w kazdej klasie osobno, bohater bedzie mial
     healthbar w rogu ekranu, a potwory miejmy nadzieje beda go mialy nad soba
    ###########################
    chcialbym na pewno, zeby byla mozliwosc najlepiej pokonania takiego przeciwnika z health barem,
    i zeby wylatywaly z niego przedmioty, np health boost,
    potem chcialbym, zeby z niego mogly wypasc losowe przedmioty.
    1:59
    dodac zycie, zeby ginely stwory i ja
    wypisywac game over jak mam 0 zycia
    2:35 03.02.2022
    kod wysprzatany, jedna ciekawa rzecz (rect movement u playera) do obgadania,
    nastepnie powinienem przekomentowac caly kod, lub obejrzec jakies tutorialki od - zyciaaa bo Mati stwierdzil ze jest to potrzebne
    ogolnie jestem zadowolony bardzo, ale tez jestem troche na kolejnych rozdrozach.
    o czym musze pamietac: efekty bloodsplata sa w poprzedniej grze, i na pewno warto ich uzyc przy rozwijaniu walki z przeciwnikiem
    poza tym, oczyscic jeszcze klase background w settings i bedzie pretty clear
    22:52 03022022
    zaimplementowalem health bar na potworze, wszystko dziala, bylo o wiele prosciej niz myslalem, kod zagniezdza sie fukncjonanosciami ktorych wczesniej uzylem,
    do zrobiena health bar na bohaterze, ale takze kolizje potwora z bronią, oraz playera z potworem
    rozpisac sobie co na siebie jak powinno oddzialywac w kolizjach, i zastanowic sie w jakich klasach kolizje beda wykorzystywane. jako ze wiekszosc rzeczy przejmuje potwor,
    to mozna go juz wyorzystac do tego a potem zrobic tak ze dawac i boleana na drawie chociazby ze jesli eslf hp spada do zera to to bedzie sie robic True i wtedy drop by sie bedzie na ziemi
    rozpierdalal i lezal
    ooo zeby tak w kurwe uekskluzywnic gre mozna dac potworom doslownie po 2, 3 przedmioty i dawac im szanse dropniecia taka mega mala ze trzeba bylo by to farmic
    , z pwotworow wpyadalaby tylko kasa i potki ktora bylaby latwa do zrobienia, a przedmioty w chuj rzadko i mega drogie u sprzedawcow i w sumie to tak i tak nie za dobre
    np ze spermojada moga wypasc bronie jacy
    *******************************************
    co jakby zrobic skrzydla wokol bohatera z hp i tak tez oprocz hp mogloby je przedstawiac wokol niego i co wiecej te recty tez
    ***********************************************999sTYlepoints idea
    23:45
    yyy tak wieenc
    zrobilem juz hp
    teraz to if ho pcost ese to true
    i moze osobna klase do monster dropow
    powoli naprawde zblizamy sie do stworzenia nastepnego potwora, moze nawet znajde kod do tworzenia grup potworow, ale raczej najpierw powinienem jeszcze rozkminic poruszanie sie potworow,
    pieniazkiccc
    ze plonacy znicz idei chce rozmawiacz Toba o ideach wyblitowac porozmawiajmy o ideach
    golden sain czyli ue
     jak do niego podejdziesz to on mowi do Ciebie
     porozmawiajmy o ideach
      a potem wrzeszczy i atakuje
      "UE EUE UE EU EUE UEE UE wydziera sie"
    text blity ogarnac
    zeby atakowali w sensie ruszali sie w strone przeciwnika
    #################################################3
    zrobic recta i wyblitowac tekst na jego wspolzednych to da efekt

    1:18
     #################################################3
    zrobic recta i wyblitowac tekst na jego wspolzednych to da efekt
    robie research do npc, inventory, itemow i podnoszenia itemow
    2:12
    a moze zamist zwyklego damage zrobic test sily pomiedzy potworem a bohaterem i rzucac kostka czy zdaja
    21;50
    code review - bullets. py
    co jesli dac broni poprostu jakies id i potem wywolywac sprajta broni po id zrobic metode w ktorej bylby wybor broni - i na ifach zrobilbym ze
    jesli id broni rowna sie 1  = to bron bedzie tym sprajtem. do przemyslenia w jakistam sposob
    --------------------------------------------------
    pozamieniac nazwy zmiennych w screen width i screen height
    -----------------------------------------------


    '''




