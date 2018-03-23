ARG python
from ${python}
COPY . /app
RUN cd /app && python setup.py install
