
# All Auth Django 🦅

Esse tutorial é sobre a biblioteca allauth que busca oferecer um aplicativo de autenticação totalmente integrado que permite autenticação local e social, com fluxos que funcionam perfeitamente!

Link da Documentação: https://docs.allauth.org/en/latest/installation/quickstart.html

### Quick Start 💨


Primeiro, instale o pacote python. Se você não precisar de nenhuma funcionalidade relacionada à conta social, instale usando:

```
pip install django-allauth
```

Caso contrário, instale usando:

```
pip install "django-allauth[socialaccount]"
```

Então, supondo que você tenha um projeto Django instalado e funcionando, adicione o seguinte ao settings.py do seu projeto:

```
AUTHENTICATION_BACKENDS = [
    
    # Necessário fazer login por nome de usuário no Django admin, independente de `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # métodos de autenticação específicos `allauth`, como login por email
    'allauth.account.auth_backends.AuthenticationBackend',
    # ... inclua os provedores que você deseja ativar:
]
```
```
INSTALLED_APPS = [
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',

    'allauth',
    'allauth.account',

    # ... inclua os provedores que você deseja ativar:
    'allauth.socialaccount',
```
```
MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    
    # Adicione o middleware da conta:
    "allauth.account.middleware.AccountMiddleware",
)

```
Verifique se o seu TEMPLATES tem isso:
```
# Especifique os processadores de contexto da seguinte forma:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Contextos relacionados ao Django já definidos aqui

                # `allauth` precisa disso do Django
                'django.template.context_processors.request',
            ],
        },
    },
]
```

Para social Accounts:

```
# Configurações específicas do provedor
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # Para cada provedor baseado em OAuth, adicione um ``SocialApp``
        # (``socialaccount`` app) contendo o cliente necessário
        # credenciais ou liste-as aqui:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
```

Além disso, adicione isto ao seu projeto urls.py:

```
urlpatterns = [

    path('accounts/', include('allauth.urls')),

]
```
### Pós instalação 

Na raiz do Django execute o comando abaixo para criar suas tabelas de banco de dados:

```
python manage.py migrate    
```