if ! command -v python &> /dev/null; then
    pip3 install -r requirements.txt
else
    pip install -r requirements.txt
fi
