FROM python:3.11-slim
WORKDIR /app
COPY . .
EXPOSE 7890
CMD ["python", "app.py"]
