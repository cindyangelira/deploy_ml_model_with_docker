FROM continuumio/anaconda3:latest

COPY . /usr/ML/app

WORKDIR /usr/ML/app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    
EXPOSE 8080

CMD python app.py
