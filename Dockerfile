ARG python
from ${python}
COPY . /app
RUN cd /app && pip install -e .[tests]
