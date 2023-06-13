FROM continuumio/anaconda3:latest
COPY . /usr/ML/app
EXPOSE 8080
WORKDIR /usr/ML/app
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
CMD python app.py