FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV SECRET_KEY=secret_key
ENV DEBUG=False
ENV ALLOWED_HOSTS=*

EXPOSE 8000

CMD ["gunicorn", "teamtracker.wsgi:application", "--bind", "0.0.0.0:8000"]
