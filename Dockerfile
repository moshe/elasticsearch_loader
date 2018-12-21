ARG python
from ${python}
RUN apk add --no-cache gcc musl-dev
COPY . /app
RUN cd /app && pip install -e .[tests]
