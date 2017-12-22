ARG python
from ${python}
RUN pip install elasticsearch click==6.7 click-conf click-stream==0.0.6 futures pytest mock
COPY . /app
RUN cd /app && python setup.py develop
