ARG python
from ${python}
ADD requirements-dev.txt /tmp/
RUN pip install -r /tmp/requirements-dev.txt
COPY . /app
RUN cd /app && python setup.py install
