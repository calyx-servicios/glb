FROM calyxodoo/odoo:13.0

USER root

COPY ./requirements.txt /etc/odoo/requirements.txt
RUN python3 -m pip install --ignore-installed -r /etc/odoo/requirements.txt

USER odoo