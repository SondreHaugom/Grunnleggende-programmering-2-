from pytest import mark, raises 
from verktoy import finn_minste_storste, reverser, er_primtall
\

"""

# Tester for finn_minste_storste-funksjonen
@mark.parametrize(
    "tall, minste, storste",
    [
        ([3, 1, 4, 1, 5, 9, 2], 1, 9),      # Vanlig liste med positive tall
        ([-5, -1, -10, -2], -10, -1),       # Bare negative tall
        ([0, 0, 0, 0], 0, 0),               # Like tall / nuller
        ([42], 42, 42),                     # Kun ett tall i listen
        ([1.5, 2.7, -0.5, 4.2], -0.5, 4.2), # Desimaltall (floats)
    ]
)




def test_finn_minste_og_storste_suksess(tall, minste, storste):
    assert finn_minste_storste(tall) == (minste, storste)
    print(f"Testet med {tall}, minste tall er {minste} og største tall er {storste}")



def test_finn_minste_og_storste_tom_liste():
    with raises(ValueError):
        finn_minste_storste([])  



# Tester for reverser-funksjonen
def test_reverser():
    assert reverser("Hello") == "olleH"


def test_reverser_tom_streng():
    assert reverser("") == ""

"""


# Tester for er_primtall-funksjonen
def test_er_primtall():
    assert er_primtall(2) == True
    assert er_primtall(4) == False

def test_er_primtall_negativt_tall():
    assert er_primtall(-5) == False