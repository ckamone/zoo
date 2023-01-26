"""
info
:return:
"""

def test_get_homepage(client):
    """
    info
    :return:
    """
    url = '/'
    response = client.get(url)
    assert response.status_code == 200


def test_get_products(client):
    """
    info
    :return:
    """
    url = '/products/'
    response = client.get(url)
    assert response.status_code == 200


def test_get_product(client):
    """
    info
    :return:
    """
    url = '/products/1/'
    response = client.get(url)
    assert response.status_code == 200
