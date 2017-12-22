ARG python
from ${python}
ADD requirements.txt /tmp/
ADD requirements-dev.txt /tmp/
RUN pip install -r /tmp/requirements.txt -r /tmp/requirements-dev.txt
COPY . /app
RUN cd /app && python setup.py develop
