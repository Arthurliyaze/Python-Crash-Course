from city_functions import *

def test_city_country():
    """Test if input as 'santiago' and 'chile' work?"""

    city_info = get_city('sandiago', 'chile', population = 5000000)
    assert city_info == 'Sandiago, Chile - population 5000000'