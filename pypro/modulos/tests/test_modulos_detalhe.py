import pytest
from django.urls import reverse
from model_mommy import mommy
from pypro.modulos.models import Modulo
from pypro.django_assertions import assert_contains


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulos(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)
