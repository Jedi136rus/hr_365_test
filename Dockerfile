FROM python:3

ENV DJANGO_SETTINGS_MODULE=hr_365_test.settings
ENV API_KEY='cur_live_XKf0Vm1furR8r1Q8WolbFzwqEzKv6bRrCuuaRvlO'

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]