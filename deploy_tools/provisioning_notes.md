Provisionamento de um novo site
===============================

## Pacotes necessários:

* nginx
* uv
* python 3.12
* git
* supervisor

Por exemplo, no Ubuntu

`sudo apt install supervisor`

## Config do Nginx Virtual Host

* veja nginx.template.conf
* substitua SITENAME pelo seu dominio

## Serviço Supervisor
* veja o gunicorn-supervisor.conf
* substitua SITENAME pelo seu dominio

## Estrutura de pastas:
Suponha q vamos utilizar o /var/www

/var/www
  └── SITENAME
    └── source