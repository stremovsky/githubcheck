FROM python:3.8-alpine
WORKDIR /code
COPY requirements.txt .
RUN addgroup -S appgroup && adduser --no-create-home -S appuser -G appgroup && \
    chown appuser:appgroup /code &&\
    pip install -r requirements.txt
COPY src src
USER appuser
CMD [ "python", "-u", "./src/check.py" ]
