FROM python
USER root

RUN pip install xmlschema
RUN pip install scipy
RUN pip install dash
RUN pip install pandas
RUN pip install dash_table
RUN pip install pyyaml
RUN pip install dash_core_components
RUN pip install dash_html_components
RUN pip install yattag

RUN mkdir UPLOADS PROJECTS ijaltexts tests tests/sampleTexts
COPY ijaltexts/* ijaltexts/
COPY tests/* tests/
COPY tests/sampleTexts/* tests/sampleTexts/

EXPOSE 8050
