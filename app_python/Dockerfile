FROM cwadley/alpine-chrony:4.1


ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add python3=3.9.5-r1 py3-pip=20.3.4-r1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT [ "/usr/bin/python3", "/app/app.py" ]
