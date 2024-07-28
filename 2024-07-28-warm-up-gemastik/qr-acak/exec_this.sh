!#/usr/bin/env bash

curl -o gemastik_5.png https://siber.gemastik.id/files/292b96c851b7338b751a7d338b90c287/gemastik_5.png?token=eyJ1c2VyX2lkIjoxNjYsInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjl9.ZqXiLA.Iw_29tjMpvHjKm_GIgpZEzeLwUk

curl -O https://raw.githubusercontent.com/rvyhvn/ctf/master/2024-07-28-warm-up-gemastik/qr-acak/solve.py
curl -O https://raw.githubusercontent.com/not-pwned-yet/ctf/master/2024-07-28-warm-up-gemastik/qr-acak/requirements.txt

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt

python3 solve.py

deactivate

