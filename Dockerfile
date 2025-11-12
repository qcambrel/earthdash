FROM mambaorg/micromamba:latest

COPY environment.yml .

RUN micromamba create --name earth --file environment.yml && \
    micromamba clean --all --yes

ENV ENV_NAME=earth

COPY app.py .
COPY driver.py .
COPY observations.yml .
COPY views.json .
COPY features ./features
COPY metrics ./metrics
COPY plotting ./plotting
COPY processing ./processing
COPY utils/ ./utils
COPY video ./video
COPY .streamlit ./.streamlit

CMD ["streamlit", "run", "app.py"]