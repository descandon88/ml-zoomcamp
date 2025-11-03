FROM agrigorev/zoomcamp-model:2025

WORKDIR /app
COPY . /app
RUN pip install uv

RUN uv pip install --system -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "serve_model:app", "--host", "0.0.0.0", "--port", "8000"]
