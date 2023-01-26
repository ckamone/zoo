def test_get_homepage(client):
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

def test_get_products(client):
    url = '/products/'
    response = client.get(url)
    assert response.status_code == 200

def test_get_product(client):
    url = '/products/1/'
    response = client.get(url)
    assert response.status_code == 200