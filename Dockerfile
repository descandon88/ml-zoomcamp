# Base image with Jupyter and Python
FROM jupyter/base-notebook:python-3.11

# Switch to root to install system dependencies
USER root

# Install any required system packages (optional)
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch back to notebook user
USER $NB_UID

# Copy requirements file (list of Python packages)
COPY requirements.txt /tmp/

# Install Python libraries
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Expose Jupyter port
EXPOSE 8888

# Default command (starts Jupyter Notebook)
CMD ["start-notebook.sh"]