import pytest
from django.urls import reverse


# Create your tests here.
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/422595352?h=9b639d54b8"')
