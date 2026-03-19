# ################################## HW1 ################################## #

from typing import Optional, List


"""
Pokyny.

- Deadline odevzdání: 15. 3. 2026 / 22. 3. 2026
- Maximum 6 bodů
- Odevzdejte pouze tento soubor doplněný o Vaše řešení
- V případě, že chcete vytvářet vlastní testy, vkládete je na příslušné místo
    na konci souboru.
    - Před odevzdáním vlastní modifikace smažte.
- Pište srozumitelný kód, používejte vhodné názvy proměnných a funkcí.
- Dodržujte standard pep8 - proveďte kontrolu pomocí pycodestyle.
- Neměňte hlavičky připravených funkcí.
- Případné nejasnosti můžete řešit v diskuzním fóru. Pokud by ale mela otázka
    obsahovat kusy kódu, nebo něco, co by mohli ostatní studenti opsat, tak
    napište raději email.
- Pokud nevíte, jak nějaký příklad vyřesit kompletně, napište do komentáře,
    co vašemu řešení chybí.
- Neopisujte. Nestojí to za to. Dostanete záporné body a budete muset úlohu
    stejně vypracovat sami.
"""


"""
ČÁST I.

V následujícím kódu jsou uvedeny tři funkce. Vaším úkolem je vypsat jejich
asymptotickou časovou složitost.

Místo uvedeného TODO doplňte složitostní třídu pro danou funkci.

Hodnocení:
*0,5 bodu za každou správě určenou složitost (maximálně tedy *1,5 bodu)

"""


def time_complexity_1(num: int = 0) -> None:
    count = 0
    i = num
    while i > 0:
        j = 1
        while j <= num:
            k = 0
            while k < num:
                if True:
                    count += 1
                    k += 2
            j *= 2
        i //= 2

    print("Časová složitost algoritmu je Theta({})".format("TODO"))


def time_complexity_2(num: int = 0) -> None:
    i = 1
    while i < num:
        j = num - 1
        while j > 0:
            k = j
            while k < num:
                if True:
                    k += 2
            j //= 2
        i *= 2

    print("Časová složitost algoritmu je Theta({})".format("TODO"))


def time_complexity_3(num: int = 0) -> None:
    i = num
    while i > 0:
        j = 1
        while j < num:
            k = 0
            while k < j:
                k += 1
            j *= 2
        i -= 1

    print("Časová složitost algoritmu je Theta({})".format("TODO"))


time_complexity_1()
time_complexity_2()
time_complexity_3()
print()


"""
ČÁST II.

Následující funkce obsahují velké množství chyb různých typů.

Vaším úkolem je projít kód a opravit jej tak, abyste všechny chyby odstranili.

Testy nemodifikujte, jsou jen pro kontrolu a to, že všechny projdou neznamená,
že je Vás kód bez chyby.

Opravujte jen funkce, které mají v komentáři TODO.

V této části není povoleno používat funkce nad řetězci
(https://www.w3schools.com/python/python_ref_string.asp).

Hodnocení:
*0,5 bodu za každou funkci (maximálně *3,5 bodu)
- Pro udělení bodů je nutné, aby algoritmus:
- byl totálně korektní (nutno řešit i okrajové případy, nesmí cyklit)
- splňoval požadovanou časovou a prostorovou složitost 

*1 bod za čistotu kódu
- dodržování PEP8
- správné pojmenovávání proměnných (anglicky a podle toho, co reprezentují)
- mezery kolem operátorů
- řádky kratší než 80 znaků
- dva volné řádky mezi funkcemi
- nepoužívání závorek tam, kde nepatří
- ...

Snažte se prosím kód opravit tak, aby neobsahoval zbytečné řádky. To ale
není v tomto úkolu hodnoceno.
 
"""


# TODO: opravit tuto funkci
def is_string_palindrom(string: str) -> bool:
    """
    Testuje, zda je zadaný řetězec (string) palindrom
    a to bez použití funkce reverse. Vrací True v případě,
    že je palindrom, jinak False.

    časová složitost: O(len(string))
    prostorová složitost: O(1)

    :param string: řetězec, který je testovaný na palindrom
    :return True pokud je řetězec palindrom, jinak False
    """
    if string is None:
        return False

    i = 0
    while i <= len(string):
        if string[i] == string[len(string) - i]:
            continue
        else:
            return False
    return True


class Node:
    """
    Třída Node slouží pro reprezentaci objektu v jednosměrné
    spojovaném seznamu.

    Atributy:
        value   reprezentuje uloženou hodnotu/objekt
        next    reference na následující prvek v seznamu
    """

    def __init__(self) -> None:
        self.value: Optional[int] = None
        self.next: Optional[Node] = None


class LinkedList:
    """
    Třída LinkedList reprezentuje spojovaný seznam.

    Atributy:
        first   reference na první prvek seznamu
    """

    def __init__(self) -> None:
        self.first: Optional[Node] = None


# TODO: opravit tuto funkci
def insert(linked_list: LinkedList, value: int) -> Node:
    """
    Funkce insert vkládá na konec seznamu (linked_list) nový uzel
    s danou hodnotou (value). Vrací referenci na nový uzel seznamu.

    časová složitost: O(počet nodů v linked_listu)
    prostorová složitost: O(1)

    :param linked_list: zřetězený seznam, do kterého se prvek vkládá
    :param value: hodnota prvku, který se vkládá
    :return: odkaz na nově vytvořený uzel seznamu
    """
    node = Node()
    node.value = value

    tmp = linked_list.first.next
    while tmp is not None:
        tmp = tmp.next

    if linked_list.first is None:
        linked_list.first = node
    else:
        tmp.next = node

    return node


# TODO: opravit tuto funkci
def delete_key(linked_list: LinkedList, key: int) -> bool:
    """
    Funkce delete_key smaže první výskyt klíče (key) v seznamu
    (linked_list). Vrátí False pokud klíč nebyl nalezen, True jinak.

    časová složitost: O(počet nodů v linked_listu)
    prostorová složitost: O(1)

    :param linked_list: zřetězený seznam, ze kterého se prvek maže
    :param key: klíč mazaného prvku
    :return: True pokud klíč byl nalezen (a smazán), False jinak
    """
    node = linked_list.first

    while node.next is not None:
        node = node.next
        previous = node
        if node.value == key:
            break

    if node is None:
        return False

    previous.next = node

    return True


# TODO: opravit tuto funkci
def multiply_numbers(bound: int, numbers: List[int]) -> int:
    """
    Funkce vypočítá součin čísel v seznamu numbers, jejichž hodnota
    je z intervalu 1 až bound (včetně). Pokud se v poli žádná taková
    čísla nenacházejí, vrátí 1.

    časová složitost: O(max(bound, len(numbers))
    prostorová složitost: O(bound)

    :param bound: horní hranice intervalu pro hodnotu čísel, která se
        započítávají do výsledku
    :param numbers: seznam čísel k počítání součinu
    :return: součin čísel v seznamu numbers, jejichž hodnota je z intervalu
        1 až bound (včetně)
    """
    array = [0 for i in range(bound)]
    for i in range(len(numbers)):
        array[numbers[i]] += 1
    val = 1
    for i in range(len(array)):
        for j in range(array[i]):
            val *= i
    return val


# TODO: opravit tuto funkci
def has_correct_parentheses(string: str) -> bool:
    """
    Funkce otestuje, zda zadaný řetězec obsahuje správné ozávorkování,
    tedy před každou uzavírací závorkou musí být příslušná otevírací.
    Řeší se pouze závorky ( ). Vrací True v případě správného
    ozávorkování, jinak False.

    časová složitost: O(len(string))
    prostorová složitost: O(1)

    :param string: testovaný řetězec
    :return: True v případě správného ozávorkování závorkami ( ), jinak False
    """
    opened = 0
    for i in range(len(string)):
        if string[i] == '(':
            opened += 1
        if string[i] == ')':
            opened -= 1
        if opened == 0:
            return True

    return False


# TODO: opravit tuto funkci
def sequence_sum(sequence: List[int]) -> int:
    """
    Funkce spočte "sumu" posloupnosti (sequence) a to tak, že pokud je
    číslo větší než předcházející (sequence[n] > sequence[n-1]), tak ho
    přičte k "sumě", pokud je sequence[n] < sequence[n-1], tak ho odečte
    a pokud je stejné, tak ho přeskočí. První číslo se nezapočítá.

    časová složitost: O(len(sequence))
    prostorová složitost: O(1)

    :param sequence: seznam čísel, pro který se má počítat speciální suma
    :return: speciální suma dle popisu funkce
    """
    strange_sum = 0
    for i in range(len(sequence)):
        if i == 0:
            continue
        if sequence[i] > sequence[i - 1]:
            strange_sum += sequence[i]
        if sequence[i] < sequence[i - 1]:
            strange_sum -= sequence[i]
    return strange_sum


# TODO: opravit tuto funkci
def find_substring(string: str, substring: str) -> int:
    """
    Funkce hledá podřetězec (substring) v řetězci (string).
    Pokud se podřetězec v řetězci nachází, vrátí index prvního výskytu.
    Jinak vrací -1.

    časová složitost: O(len(string) * len(substring))
    prostorová složitost: O(1)

    :param string: neprázdný řetězec, jenž se prohledává
    :param substring: neprázdný podřetězec, který se hledá v řetězci 'string'
    :return: Pokud se podřetězec v řetězci nachází, vrátí index prvního
        výskytu. V opačném případě vrací -1.
    """
    if len(substring) > len(string):
        return -1

    j = 1
    i = 1
    while i < len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return i - j
            j += 1
    i += 1
    return -1


########################################################################
#               Následuje kód testů                                    #
########################################################################

def ib114_test_palindrom() -> None:
    test_cases = [("abccba", True), ("abcba", True), ("abcabc", False)]

    for i, case in enumerate(test_cases):
        print("Test {} palindrom: je {} palindrom?".format(i + 1, case[0]))
        try:
            my_res = is_string_palindrom(case[0])
            if my_res == case[1]:
                print("OK.")
            else:
                if case[1]:
                    print("NOK, {} {} palindrom, ale program vrací {}.".
                          format(case[0], "je" if case[1] else "neni", my_res))

        except IndexError as exc:
            print("NOK: přístup mimo pole.")
            print("Chybová hláška Pythonu: {}".format(exc))


def ib114_test_list() -> None:
    try:
        list1 = LinkedList()
        list1.first = None
        print("Test 1 list: vkládání 1. prvku do listu.")
        tmp1 = insert(list1, 1)
        if tmp1.value == 1 and list1.first == tmp1 and tmp1.next is None:
            print("OK.")
        else:
            print("NOK, vložení prvního prvku neproběhlo v pořádku,",
                  "zkontrolujte, zda je správně nastavena hodnota",
                  "a reference next.")
    except AttributeError as exc:
        print("NOK: špatná práce s pamětí.")
        print("Chybová hláška Pythonu: {}".format(exc))

    try:
        print("Test 2 list: vkládání 2. prvku do listu.")
        list2 = LinkedList()
        tmp21 = insert(list2, 1)
        tmp22 = insert(list2, 2)
        if (tmp22.value == 2 and list2.first == tmp21 and
                tmp22.next is None and tmp21.next == tmp22):
            print("OK.")
        else:
            print("NOK, vložení druhého prvku neproběhlo v pořádku,",
                  "zkontrolujte, zda je správně nastavena hodnota",
                  "a reference next.")
    except AttributeError as exc:
        print("NOK: špatná práce s pamětí.")
        print("Chybová hláška Pythonu: {}".format(exc))

    try:
        print("Test 3 list: odstranění 2. prvku z listu.")
        list3 = LinkedList()
        tmp3 = insert(list3, 1)
        insert(list3, 2)
        if delete_key(list3, 2) and tmp3.next is None:
            print("OK.")
        else:
            print("NOK, neodstranili jste prvek,",
                  "může to být dáno i špatným vkládáním.")
    except AttributeError as exc:
        print("NOK: špatná práce s pamětí.")
        print("Chybová hláška Pythonu: {}".format(exc))

    try:
        print("Test 4 list: odstranění prvku z prázdného listu.")
        list3 = LinkedList()
        if delete_key(list3, 2):
            print("NOK, odstranili jste prvek z prázdného listu",
                  "nebo vrátili True")
        else:
            print("OK.")
    except AttributeError as exc:
        print("NOK: špatná práce s pamětí.")
        print("Chybová hláška Pythonu: {}".format(exc))

    try:
        print("Test 5 list: odstranění chybějícího prvku z listu.")
        list3 = LinkedList()
        insert(list3, 1)
        insert(list3, 2)
        if delete_key(list3, 4):
            print("NOK, odstranili jste prvek, který v listu nebyl",
                  "nebo vrátili True")
        else:
            print("OK.")
    except AttributeError as exc:
        print("NOK: špatná práce s pamětí.")
        print("Chybová hláška Pythonu: {}".format(exc))


def ib114_test_multiply_numbers() -> None:
    test_cases = [(1, [1, 1, 1], 1), (2, [3, 3, 3], 1), (3, [1, 1, 2], 2),
                  (3, [1, 4, 3], 3), (4, [3, 3, 3, 2], 54), (3, [3, 3, 4], 9)]

    for i, case in enumerate(test_cases):
        print("Test {} multiply numbers: multiply_numbers({}, {})".format(
            i + 1, case[0], case[1]))

        try:
            res = multiply_numbers(case[0], case[1])
            if res != case[2]:
                print("NOK: {} != {}".format(res, case[2]))
            else:
                print("OK.")
        except IndexError as exc:
            print("NOK: přístup mimo pole.")
            print("Chybová hláška Pythonu: {}".format(exc))


def ib114_test_brackets() -> None:
    test_cases = [("()", True), (")(", False), ("aaa", True), ("((", False)]

    for i, case in enumerate(test_cases):
        print("Test {} závorkování: vstup {}".format(i + 1, case[0]))
        try:
            if has_correct_parentheses(case[0]) == case[1]:
                print("OK.")
            else:
                print("NOK, {} {} správné uzávorkování a funkce vrátí {}".
                      format(case[0], "je" if case[1] else "není",
                             not case[1]))
        except IndexError as exc:
            print("NOK: přístup mimo pole.")
            print("Chybová hláška Pythonu: {}".format(exc))


def ib114_test_sequence_sum() -> None:
    test_case = [([1, 2, 3], 5), ([1, 2, 1], 1), ([1, 2, 2], 2)]

    for i, case in enumerate(test_case):
        print("Test {}: sequence_sum({})".format(i + 1, case[0]))
        try:
            res = sequence_sum(case[0])
            if res == case[1]:
                print("OK.")
            else:
                print("NOK, sequence_sum({}) je {} a Vám vyšlo {}".format(
                    case[0], case[1], res))
        except IndexError as exc:
            print("NOK: přístup mimo pole.")
            print("Chybová hláška Pythonu: {}".format(exc))


def ib114_test_find() -> None:
    test_cases = [("abc", "abc", 0), ("abc", "b", 1), ("abcb", "abb", -1),
                  ("ab", "bb", -1), ("ababcb", "abcb", 2)]

    for i, case in enumerate(test_cases):
        print("Test {}: je v '{}' podřetězec '{}'?".format(i + 1, case[0],
                                                           case[1]))
        try:
            res = find_substring(case[0], case[1])
            if res == case[2]:
                print("OK.")
            else:
                print("NOK, podřetězec je na pozici {}, vy vracíte {}".
                      format(case[2], res))
        except IndexError as exc:
            print("NOK: přístup mimo pole.")
            print("Chybová hláška Pythonu: {}".format(exc))


if __name__ == '__main__':
    print("Testy netestují vše. Pokud Vám tedy prošly všude na OK,")
    print("neznamená to, že v implementaci nemůže být chyba, kterou testy ")
    print("nezachytily. To, že je nějaký test NOK ale znamená,")
    print("že máte něco špatně.")
    print()

    ib114_test_palindrom()
    print()
    ib114_test_list()
    print()
    ib114_test_multiply_numbers()
    print()
    ib114_test_brackets()
    print()
    ib114_test_sequence_sum()
    print()
    ib114_test_find()
