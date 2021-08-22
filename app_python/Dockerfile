FROM cwadley/alpine-chrony:4.1


ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN apk add python3 py3-pip
RUN pip install --cache-dir=/cache -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT [ "/usr/bin/python3", "/app/app.py" ]
