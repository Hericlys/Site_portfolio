import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 100
CAMINHO_CAPA = os.path.join(DJANGO_BASE_DIR, "utils/capas_projetos_teste")

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker
    from portfolio.models import CategoriaProjeto, Projeto

    categorais = CategoriaProjeto.objects.all()
    nome_capa = ['capa1', 'capa2', 'capa3', 'capa4', 'capa5']

    fake = faker.Faker('pt_BR')

    django_projetos = []

    for _ in range(NUMBER_OF_OBJECTS):
        nome = fake.text(max_nb_chars=100)
        categoria = choice(categorais)
        capa = os.path.join(CAMINHO_CAPA, choice(nome_capa))
        descricao = fake.text(max_nb_chars=100)
        conteudo = fake.text(max_nb_chars=400)

        django_projetos.append(
            Projeto(
                nome=nome,
                categoria=categoria,
                capa=capa,
                descricao=descricao,
                conteudo=conteudo 
            )
        )

    if len(django_projetos) > 0:
         Projeto.objects.bulk_create(django_projetos)
